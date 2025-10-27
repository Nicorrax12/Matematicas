<?php
session_start();
require_once '../conexion.php';

if (!isset($_SESSION['usuarioid'])) {
    header('Location: ../usuario/login.php');
    exit;
}

// Consultar exámenes creados por el usuario
$stmt = $conn->prepare("SELECT id, titulo, fecha_creacion FROM examenes WHERE creador_id = ? ORDER BY fecha_creacion DESC");
$stmt->execute([$_SESSION['usuarioid']]);
$examenes = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mis Exámenes | Panel</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {background:linear-gradient(115deg,#11151c 40%,#0c353c 100%);
            min-height:100vh;margin:0;font-family:'Segoe UI',Arial,sans-serif;color:#acffed;}
        .panel-admin {margin:54px auto 0 auto;background:rgba(16,28,44,0.96);border:2px solid #09fbd3;box-shadow:0 8px 38px #1afbf233; border-radius:18px;padding:35px 22px 28px 22px;max-width:470px;}
        h1 {color:#09fbd3;text-shadow:0 0 8px #35ffffa7;}
        table {width:100%;margin-top:15px;border-collapse:collapse;}
        th,td {padding:10px 6px;color:#d0fff7;}
        th {background:#0c353c89;color:#35fff5;}
        tr:nth-child(even){background:rgba(3,35,32,0.27);}
        tr:hover {background:#14ffd366;}
        .enlace {margin-top:18px;text-align:center;}
        .enlace a {color:#09fbd3;font-weight:600;text-decoration:none;}
        .enlace a:hover {color:#35fff5;}
    </style>
</head>
<body>
<div class="panel-admin">
    <h1>Mis Exámenes</h1>
    <table>
        <tr>
            <th>ID</th><th>Título</th><th>Fecha de creación</th>
        </tr>
        <?php foreach($examenes as $ex): ?>
            <tr>
                <td><?php echo htmlspecialchars($ex['id']); ?></td>
                <td><?php echo htmlspecialchars($ex['titulo']); ?></td>
                <td><?php echo htmlspecialchars($ex['fecha_creacion']); ?></td>
            </tr>
        <?php endforeach; ?>
    </table>
    <div class="enlace">
        <a href="crear_examen.php">Crear nuevo examen</a> |
        <a href="../index.php">Menú principal</a>
    </div>
</div>
</body>
</html>
