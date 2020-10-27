class Person {
  public $first_name,$last_name;
  public function __construct($first_name,$last_name) {
    $this->first_name = $first_name;
    $this->last_name = $last_name;
  }
  public function get_full_name() {
    return $this->first_name." ".$this->last_name; // The $this keyword can also be used in other methods to refer to the object itself
  }
}