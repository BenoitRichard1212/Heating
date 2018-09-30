<?php
	namespace classes;

	class Room
	{
		private $m_roomName;
		private $m_roomMaxTemp;
		private $m_roomMinTemp;
		private $m_roomSensorName;
		private $m_roomSensorFloorName;
		private $m_roomRelayName;
		private $m_currentTemp;
		private $m_currentFloorTemp;
		public function __construct($p_roomName, $p_roomMaxTemp, $p_roomMinTemp, $p_roomSensorName, $p_roomSensorFloorName, $p_roomRelayName)
		{
			$this->m_roomName = $p_roomName;
			$this->m_roomMaxTemp = $p_roomMaxTemp;
			$this->m_roomMinTemp = $p_roomMinTemp;
			$this->m_roomSensorName = $p_roomSensorName;
			$this->m_roomSensorFloorName = $p_roomSensorFloorName;
			$this->m_roomRelayName = $p_roomRelayName;
			$this->m_currentTemp = 0;
			$this->m_currentFloorTemp = 0;
		}

		//GETTER's
		public function getRoomName()
		{
			return $this->m_roomName;
		}

		public function getRoomMaxTemp()
		{
			return $this->m_roomMaxTemp;
		}

		public function getRoomMinTemp()
		{
			return $this->m_roomMinTemp;
		}

		public function getRoomSensorName()
		{
			return $this->m_roomSensorName;
		}

		public function getRoomSensorFloorName()
		{
			return $this->m_roomSensorFloorName;
		}

		public function getRoomRelayName()
		{
			return $this->m_roomRelayName;
		}

		public function getRoomCurrentTemp()
		{
			return $this->m_currentTemp;
		}

		public function getRoomCurrentFloorTemp()
		{
			return $this->m_currentFloorTemp;
		}

		//SETTER's
		public function setRoomName($p_roomName)
		{
			$this->m_roomName = $p_roomName;
		}

		public function setRoomMaxTemp($p_roomMaxTemp)
		{
			$this->m_roomMaxTemp = $p_roomMaxTemp;
		}

		public function setRoomMinTemp($p_roomMinTemp)
		{
			$this->m_roomMinTemp = $p_roomMinTemp;
		}

		public function setRoomSensorName($p_roomSensorName)
		{
			$this->m_roomSensorName = $p_roomSensorName;
		}

		public function setRoomSensorFloorName($p_roomSensorFloorName)
		{
			$this->m_roomSensorFloorName = $p_roomSensorFloorName;
		}

		public function setRoomRelayName($p_roomRelayName)
		{
			$this->m_roomRelayName = $p_roomRelayName;
		}

		public function setCurrentRoomTemp($p_roomCurrentTemp)
		{
			$this->m_roomSensorFloorName = $p_roomCurrentTemp;
		}

		public function setCurrentFlooreTemps($p_roomCurrentFloorTemp)
		{
			$this->m_roomRelayName = $p_roomCurrentFloorTemp;
		}
}		

