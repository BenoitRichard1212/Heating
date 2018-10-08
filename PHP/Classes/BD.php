<?php
	namespace classes;

	require_once("Room.php");

	use classes\Room;

	class BD
	{
		private $m_rooms = array();
		private $m_host = 'localhost';
		private $m_user = 'root';
		private $m_password = '';
		private $m_db = 'heating';	
		private $m_conn;	

		private function connectionBd()
		{
			$this->m_conn = new \mysqli($this->m_host, $this->m_user, $this->m_password, $this->m_db);
			
			if ($this->m_conn->connect_error) {
				die($this->m_conn->connect_error);
			}
		}

		private function fermetureConnectionBd()
		{
			$this->m_conn->close();
		}

		//Load all the rooms.
		public function getAllRooms()
		{
			$this->connectionBd();

			$stmt = $this->m_conn->prepare("SELECT * FROM rooms");
			$stmt->execute();
			$result = $stmt->get_result();
			if($result->num_rows === 0) exit('No rows');
			while($row = $result->fetch_assoc()) {
			  $room = new Room($row['Room_name'], $row['Max_temp'], $row['Min_temp'], $row['Sensor_room_name'], $row['Sensor_floor_name'], $row['Relay_name']);
			  array_push($this->m_rooms, $room);
			}
			$stmt->close();

		    $this->fermetureConnectionBd();

		    return $this->m_rooms;
   		}

   		//Get a single room.
		public function getRoom($p_roomName)
		{
			$this->connectionBd();
			$room = NULL;

			if($stmt = $this->m_conn->prepare("SELECT Room_name, Max_temp, Min_temp, Sensor_room_name, Sensor_floor_name, Relay_name FROM rooms WHERE Room_name = ?")) {

				$stmt->bind_param("s", $p_roomName);
	   			$stmt->execute(); 
	   			$stmt->bind_result($roomName, $roomMaxTemp, $roomMinTemp, $roomSensorName, $roomSensorFloorName, $roomRelayName);

	   			while ($stmt->fetch()) {
			    	$room = new Room($roomName, $roomMaxTemp, $roomMinTemp, $roomSensorName, $roomSensorFloorName, $roomRelayName);
		    	}

		    $stmt->close();
			}

			$this->fermetureConnectionBd();
			return $room;
		}
	}
	