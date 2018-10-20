<?php
	namespace classes;

	class Sensor
	{
		private $m_sensor;
		private $m_temperature;
        private $m_humidity;
		public function __construct($p_sensor, $p_temperature, $p_humidity)
        {
			$this->m_sensor = $p_sensor;
			$this->m_temperature = $p_temperature;
            $this->m_humidity = $p_humidity;
		}

		//GETTER's
		public function getSensor()
		{
			return $this->m_sensor;
		}

		public function getTemperature()
		{
			return $this->m_temperature;
		}

		public function getHumidity()
		{
			return $this->m_humidity;
		}

		//SETTER's
		public function setSensor($p_sensor)
		{
			$this->m_sensor = $p_sensor;
		}

		public function setTemperature($p_temperature)
		{
			$this->m_temperature = $p_temperature;
		}

		public function setHumidity($p_humidity)
		{
			$this->m_humidity = $p_humidity;
		}
}		

