<?php
date_default_timezone_set('America/Los_Angeles');

$secret = "151020dd1e6e653f01a1f596e1a5a7e51444826a7c27eb137fa823ac9b751352";

$embedpath= "/embed/dashboards/40?Select%20Date%20Range=2020%2F02%2F01%20to%202020%2F04%2F30&filter_config=%7B%22Select%20Date%20Range%22:%5B%7B%22type%22:%22between%22,%22values%22:%5B%7B%22date%22:%222020-02-01T00:00:00.000Z%22,%22tz%22:true%7D,%7B%22date%22:%222020-04-30T00:00:00.000Z%22,%22tz%22:true%7D%5D,%22id%22:2%7D%5D%7D";

$host = "quantiphi.looker.com";
$path = "/login/embed/" . urlencode($embedpath);

$json_nonce = json_encode(md5(uniqid()));
$json_current_time = json_encode(time());
$json_session_length = json_encode(3600);
$json_external_user_id = json_encode("test_user");
$json_first_name = json_encode("John");
$json_last_name = json_encode("Doe");
$json_permissions = json_encode( array ( "see_user_dashboards", "see_lookml_dashboards", "access_data", "see_looks" ) );
$json_models = json_encode( array ( "covid_cci" ) );
//$json_group_ids = json_encode( array ( 4, 2 ) );  // just some example group ids
//$json_external_group_id = json_encode("awesome_engineers");
//$json_user_attributes = json_encode( array ( "an_attribute_name" => "my_value", "my_number_attribute" => "0.231" ) );  // just some example attributes
// NOTE: accessfilters must be present and be a json hash. If you don't need access filters then the php
// way to make an empty json hash as an alternative to the below seems to be:
// $accessfilters = new stdClass()
//$accessfilters = array (
//  "<your_model_name>"  =>  array ( "view_name.dimension_name" => "<value>" )
//);
//$json_accessfilters = json_encode($accessfilters);

$stringtosign = "";
$stringtosign .= $host . "\n";
$stringtosign .= $path . "\n";
$stringtosign .= $json_nonce . "\n";
$stringtosign .= $json_current_time . "\n";
$stringtosign .= $json_session_length . "\n";
$stringtosign .= $json_external_user_id . "\n";
$stringtosign .= $json_permissions . "\n";
$stringtosign .= $json_models;
//$stringtosign .= $json_group_ids . "\n";
//$stringtosign .= $json_external_group_id . "\n";
//$stringtosign .= $json_user_attributes . "\n";
//$stringtosign .= $json_accessfilters;

$signature = trim(base64_encode(hash_hmac("sha1", utf8_encode($stringtosign), $secret, $raw_output = true)));
// , $raw_output = true

$queryparams = array (
    'nonce' =>  $json_nonce,
    'time'  =>  $json_current_time,
    'session_length'  =>  $json_session_length,
    'external_user_id'  =>  $json_external_user_id,
    'permissions' =>  $json_permissions,
    'models'  =>  $json_models,
    //'group_ids' => $json_group_ids,
    //'external_group_id' => $json_external_group_id,
    //'user_attributes' => $json_user_attributes,
    //'access_filters'  =>  $json_accessfilters,
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
echo $final;
echo "\n";
?>
