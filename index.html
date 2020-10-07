<html>
<title>Contact Center Insights</title>
<head>
<style>

/* Style the tab */
.tab {
  overflow: hidden;
  border: 1px solid #ccc;
  background-color: #f1f1f1;
}

/* Style the buttons that are used to open the tab content */
.tab button {
  background-color: inherit;
  float: left;
  border: none;
  outline: none;
  cursor: pointer;
  padding: 14px 16px;
  transition: 0.3s;
}

/* Change background color of buttons on hover */
.tab button:hover {
  background-color: #ddd;
}

/* Create an active/current tablink class */
.tab button.active {
  background-color: #ccc;
}

/* Style the tab content */
.tabcontent {
  display: none;
  padding: 6px 12px;
  border: 1px solid #ccc;
  border-top: none;
}

</style>

<script type="text/javascript">
   function openCity(evt, cityName) {
  	// Declare all variables
  	var i, tabcontent, tablinks;

  	// Get all elements with class="tabcontent" and hide them
  	tabcontent = document.getElementsByClassName("tabcontent");
  	for (i = 0; i < tabcontent.length; i++) {
    		tabcontent[i].style.display = "none";
  	}

  	// Get all elements with class="tablinks" and remove the class "active"
  	tablinks = document.getElementsByClassName("tablinks");
  	for (i = 0; i < tablinks.length; i++) {
    		tablinks[i].className = tablinks[i].className.replace(" active", "");
  	}

  	// Show the current tab, and add an "active" class to the button that opened the tab
  	document.getElementById(cityName).style.display = "block";
  	evt.currentTarget.className += " active";
}
</script>
</head>
<body>

<?php

$secret = "151020dd1e6e653f01a1f596e1a5a7e51444826a7c27eb137fa823ac9b751352";

$embedpath= "embed/dashboards/40?Select%20Date%20Range=2020%2F02%2F01%20to%202020%2F04%2F30&filter_config=%7B%22Select%20Date%20Range%22:%5B%7B%22type%22:%22between%22,%22values%22:%5B%7B%22date%22:%222020-02-01T00:00:00.000Z%22,%22tz%22:true%7D,%7B%22date%22:%222020-04-30T00:00:00.000Z%22,%22tz%22:true%7D%5D,%22id%22:2%7D%5D%7D";

$host = "quantiphi.looker.com";
$path = "/login/embed/" . urlencode($embedpath);

$json_nonce = json_encode(md5(uniqid()));
$json_current_time = json_encode(time());
$json_session_length = json_encode(900);
$json_external_user_id = "57";
$json_first_name = json_encode("John");
$json_last_name = json_encode("Doe");
$json_permissions = json_encode( array ( 'see_lookml_dashboards', 'access_data','see_user_dashboards' ) );
$json_models = json_encode( array ( "covid_cci" ) );
$json_group_ids = json_encode( array ( ) );  // just some example group ids
$json_external_group_id = json_encode("");
$user_attributes = new stdClass();
$json_user_attributes = json_encode($user_attributes);  // just some example attributes
// NOTE: accessfilters must be present and be a json hash. If you don't need access filters then the php
// way to make an empty json hash as an alternative to the below seems to be:
$accessfilters = new stdClass();
//$accessfilters = array (
//  "<your_model_name>"  =>  array ( "view_name.dimension_name" => "<value>" )
//);
$json_accessfilters = json_encode($accessfilters);

$stringtosign = "";
$stringtosign .= $host . "\n";
$stringtosign .= $path . "\n";
$stringtosign .= $json_nonce . "\n";
$stringtosign .= $json_current_time . "\n";
$stringtosign .= $json_session_length . "\n";
$stringtosign .= $json_external_user_id . "\n";
$stringtosign .= $json_permissions . "\n";
$stringtosign .= $json_models . "\n";
$stringtosign .= $json_group_ids . "\n";
$stringtosign .= $json_external_group_id . "\n";
$stringtosign .= $json_user_attributes . "\n";
$stringtosign .= $json_accessfilters;

$signature = trim(base64_encode(hash_hmac("sha1", utf8_encode($stringtosign), $secret, $raw_output = true)));
// , $raw_output = true

$queryparams = array (
    'nonce' =>  $json_nonce,
    'time'  =>  $json_current_time,
    'session_length'  =>  $json_session_length,
    'external_user_id'  =>  $json_external_user_id,
    'permissions' =>  $json_permissions,
    'models'  =>  $json_models,
    'group_ids' => $json_group_ids,
    'external_group_id' => $json_external_group_id,
    'user_attributes' => $json_user_attributes,
    'access_filters'  =>  $json_accessfilters,
    'first_name'  =>  $json_first_name,
    'last_name' =>  $json_last_name,
    'force_logout_login'  =>  false,
    'signature' =>  $signature
);

$querystring = "";
foreach ($queryparams as $key => $value) {
  if (strlen($querystring) > 0) {
    $querystring .= "&";
  }
  if ($key == "force_logout_login") {
    $value = "true";
  }
  $querystring .= "$key=" . urlencode($value);
}

$final = "https://" . $host . $path . "?" . $querystring;
?>

<!-- Tab links -->
<div class="tab">
  <button class="tablinks" onclick="openCity(event, 'London')">London</button>
  <button class="tablinks" onclick="openCity(event, 'Paris')">Paris</button>
  <button class="tablinks" onclick="openCity(event, 'Tokyo')">Tokyo</button>
</div>

<!-- Tab content -->
<div id="London" class="tabcontent">
  <iframe align="center" width="80%" height="80%" src="$final" frameborder="yes" scrolling="yes" name="myFrame" id="myFrame"></iframe>
</div>

<div id="Paris" class="tabcontent">
  <iframe align="center" width="80%" height="80%" src="$final" frameborder="yes" scrolling="yes" name="myFrame" id="myFrame"></iframe>
</div>

<div id="Tokyo" class="tabcontent">
  <iframe align="center" width="80%" height="80%" src="$final" frameborder="yes" scrolling="yes" name="myFrame" id="myFrame"></iframe>
</div>

</body>
</html>
