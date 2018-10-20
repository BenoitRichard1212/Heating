<?php
	namespace classes;

	class Room
	{
		private $m_name;
		private $m_tempMin;
		private $m_sensorFloor;
		private $m_sensorWall;
		private $m_relay;
		public function __construct($p_name, $p_tempMin, $p_sensorFloor, $p_sensorWall, $p_relay)
		}
			$this->m_name = $p_name;
			$this->m_tempMin = $p_tempMin;
			$this->m_sensorFloor = $p_sensorFloor;
			$this->m_sensorWall = $p_sensorWall;
			$this->m_relay = $p_relay;
		}

		//GETTER's
		public function getName()
		{
			return $this->m_name;
		}

		public function getTempMin()
		{
			return $this->m_tempMin;
		}

		public function getSensorFloor()
		{
			return $this->m_sensorFloor;
		}

		public function getSensorWall()
		{
			return $this->m_sensorWall;
		}

		public function getRelay()
		{
			return $this->m_relay;
		}

		//SETTER's
		public function setName($p_name)
		{
			$this->m_name = $p_name;
		}

		public function setTempMin($p_tempMin)
		{
			$this->m_tempMin = $p_tempMin;
		}

		public function setSensorFloor($p_sensorFloor)
		{
			$this->m_sensorFloor = $p_sensorFloor;
		}

		public function setSensorWall($p_sensorWall)
		{
			$this->m_sensorWall = $p_sensorWall;
		}

		public function setRelay($p_relay)
		{
			$this->m_relay = $p_relay;
		}
}		

