<?php
	namespace classes;

	class Relay
	{
		private $m_name;
		private $m_status;
        private $m_gpio;
		public function __construct($p_name, $p_status, $p_gpio)
        {
			$this->m_name = $p_name;
			$this->m_status = $p_status;
            $this->m_gpio = $p_gpio;
            $this->m_type = $p_type;
		}

		//GETTER's
		public function getName()
		{
			return $this->m_name;
		}

		public function getStatus()
		{
			return $this->m_status;
		}

		public function getGpio()
		{
			return $this->m_gpio;
		}

		public function getType()
		{
			return $this->m_type;
		}

		//SETTER's
		public function setName($p_name)
		{
			$this->m_name = $p_name;
		}

		public function setStatus($p_status)
		{
			$this->m_status = $p_status;
		}

		public function setGpio($p_gpio)
		{
			$this->m_gpio = $p_gpio;
		}

		public function setType($p_type)
		{
			$this->m_type = $p_type;
		}
}		

