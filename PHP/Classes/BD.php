<?php
	namespace classes;

	require_once("Room.php");

	use classes\Room;

	class BD
	{
		private $m_rooms = array();
		private $m_host = '192.168.0.132';
		private $m_user = 'logger';
		private $m_password = 'password';
		private $m_db = 'temperatures';	
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
			  $room = new Room($row['name'], $row['temp_min'], $row['sensor_floor'], $row['sensor_wall'], $row['relay']);
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

			if($stmt = $this->m_conn->prepare("SELECT name, temp_min, sensor_floor, sensor_wall, relay FROM rooms WHERE name = ?")) {

				$stmt->bind_param("s", $p_roomName);
	   			$stmt->execute(); 
	   			$stmt->bind_result($name, $temp_min, $sensor_floor, $sensor_wall, $relay);

	   			while ($stmt->fetch()) {
			    	$room = new Room($name, $temp_min, $sensor_floor, $sensor_wall, $relay);
		    	}

		    $stmt->close();
			}

			$this->fermetureConnectionBd();
			return $room;
		}
	}
	
