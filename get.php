<?php

header('Access-Control-Allow-Origin: *');
header("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept");
header('Access-Control-Allow-Methods: GET');
header('Content-Type: application/json; charset=utf-8');

require_once 'conexion.php';

if (!isset(getallheaders()["Authorization"]) || getallheaders()["Authorization"] != Conexion::apikey()) {

    $json = array(
        'status' => 401,
        'results' => 'No esta autorizado para hacer esta peticion'
    );
    
    echo json_encode($json, http_response_code($json["status"]));

    return;

}

if ($_SERVER['REQUEST_METHOD'] === 'GET') {

    $sql = "SELECT * FROM medidas";

    $stmt = Conexion::conectar()->prepare($sql);

    try {

        $stmt -> execute();

    } catch (PDOException $e) {
        
        return null;

    }

    $response = $stmt -> fetchAll(PDO::FETCH_CLASS);

    if (!empty($response)) {

        $json = array(
            'status' => 200,
            'total' => count($response),
            'results' => $response
        );
        
        echo json_encode($json, http_response_code($json["status"]));

    }else {

        $json = array(
            'status' => 404,
            'results' => 'Not Found'
        );

        echo json_encode($json, http_response_code($json["status"]));

    }
} else {

    $json = array(
        'status' => 405,
        'results' => 'Método no permitido'
    );

    echo json_encode($json, http_response_code($json["status"]));

}