<?php
	namespace classes;

	class GlobalSetting
	{
		private $m_name;
		private $m_value;
		public function __construct($p_name, $p_value)
        {
			$this->m_name = $p_name;
			$this->m_value = $p_value;
		}

		//GETTER's
		public function getName()
		{
			return $this->m_name;
		}

		public function getValue()
		{
			return $this->m_value;
		}

		//SETTER's
		public function setName($p_name)
		{
			$this->m_name = $p_name;
		}

		public function setValue($p_value)
		{
			$this->m_value = $p_value;
		}
}		

