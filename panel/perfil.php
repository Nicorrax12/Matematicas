<?php
session_start();
if (!isset($_SESSION['usuarioid'])) {
    header('Location: ../usuario/login.php');
    exit;
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Perfil | Panel</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {background:linear-gradient(115deg,#151e2e 40%,#14364d 100%);min-height:100vh;margin:0;font-family:'Segoe UI',Arial,sans-serif;color:#affcf5;display:flex;flex-direction:column;align-items:center;}
        .panel-perfil {background:rgba(23,38,67,0.96);border:2px solid #09fbd3;box-shadow:0 8px 38px #1afbf233;border-radius:19px;padding:38px 32px;max-width:400px;margin-top:66px;}
        h1 {color:#09fbd3;text-shadow:0 0 8px #09fbd3a8;}
        .dato {color:#fff;padding:7px 0;font-size:1.1em;}
        .enlace {margin-top:14px;text-align:center;}
        .enlace a {color:#09fbd3;text-decoration:none;font-weight:600;}
        .enlace a:hover {color:#3fffd3;}
    </style>
</head>
<body>
<div class="panel-perfil">
    <h1>Mi perfil</h1>
    <div class="dato"><b>Usuario:</b> <?php echo htmlspecialchars($_SESSION['nombre']); ?></div>
    <div class="dato"><b>Email:</b> <?php echo htmlspecialchars($_SESSION['email']); ?></div>
    <div class="enlace">
        <a href="../index.php">Menú principal</a>
    </div>
</div>
</body>
</html>
