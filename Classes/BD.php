<?php
	namespace classes;

	require_once("Room.php");
    require_once("Relay.php");
    require_once("Sensor.php");

	use classes\Room;
    use classes\Relay;
    use classes\Sensor;

	class BD
	{
		private $m_rooms = array();
        private $m_sensors = array();
        private $m_relays = array();
        private $m_globalSettings = array();
		private $m_host = '192.168.0.131';
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
        
        //Get a single sensor.
        public function getSensor($p_sensorName)
        {
            $this->connectionBd();
            $sensor = NULL;
            
            if($stmt = $this->m_conn->prepare("SELECT sensor, temperature, humidity FROM temperaturedata WHERE sensor = ?")) {
                $stmt->bind_param("s", $p_sensorName);
                $stmt->execute();
                $stmt->bind_result($sensor, $temperature, $humidity);
                while ($stmt->fetch()) {
                    $sensor = new Sensor($sensor, $temperature, $humidity);
                }
                $stmt->close();
            }
            
            $this->fermetureConnectionBd();
            return $sensor;
        }
        
        //Load all the sensors.
        public function getAllSensors()
        {
            $this->connectionBd();
            
            $stmt = $this->m_conn->prepare("SELECT * FROM temperaturedata");
            $stmt->execute();
            $result = $stmt->get_result();
            if($result->num_rows === 0) exit('No rows');
            while($row = $result->fetch_assoc()) {
                $sensor = new Sensor($row['sensor'], $row['temperature'], $row['humidity']);
                array_push($this->m_sensors, $sensor);
            }
            $stmt->close();
            
            $this->fermetureConnectionBd();
            
            return $this->m_sensors;
        }
        
        //Get a single relay.
        public function getRelay($p_relayName)
        {
            $this->connectionBd();
            $relay = NULL;
            
            if($stmt = $this->m_conn->prepare("SELECT name, status, gpio FROM relays WHERE name = ?")) {
                $stmt->bind_param("s", $p_relayName);
                $stmt->execute();
                $stmt->bind_result($name, $status, $gpio);
                while ($stmt->fetch()) {
                    $relay = new Relay($name, $status, $gpio);
                }
                $stmt->close();
            }
            
            $this->fermetureConnectionBd();
            return $relay;
        }
        
        //Load all the relays.
        public function getAllRelays()
        {
            $this->connectionBd();
            
            $stmt = $this->m_conn->prepare("SELECT * FROM relays");
            $stmt->execute();
            $result = $stmt->get_result();
            if($result->num_rows === 0) exit('No rows');
            while($row = $result->fetch_assoc()) {
                $relay = new Relay($row['name'], $row['status'], $row['gpio']);
                array_push($this->m_relays, $relay);
            }
            $stmt->close();
            
            $this->fermetureConnectionBd();
            
            return $this->m_relays;
        }

        //Get all global settings
        public function getAllGlobalSettings()
        {
            $this->connectionBd();
            
            $stmt = $this->m_conn->prepare("SELECT * FROM global_settings");
            $stmt->execute();
            $result = $stmt->get_result();
            if($result->num_rows === 0) exit('No rows');
            while($row = $result->fetch_assoc()) {
                $globalSetting = new globalSetting($row['name'], $row['value']);
                array_push($this->m_globalSettings, $globalSettings);
            }
            $stmt->close();
            
            $this->fermetureConnectionBd();
            
            return $this->m_globalSettings;
        }

        //Get a single global setting.
        public function getGlobalSetting($p_name)
        {
            $this->connectionBd();
            $globalSetting = NULL;
            
            if($stmt = $this->m_conn->prepare("SELECT name, value FROM global_settings WHERE name = ?")) {
                $stmt->bind_param("s", $p_name);
                $stmt->execute();
                $stmt->bind_result($name, $value);
                while ($stmt->fetch()) {
                    $globalSetting= new globalSettings($name, $value);
                }
                $stmt->close();
            }
            
            $this->fermetureConnectionBd();
            return $globalSetting;
        }
	}
	
