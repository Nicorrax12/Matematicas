<?php
session_start();
require_once '../conexion.php';

if (!isset($_SESSION['usuarioid'])) {
    header('Location: ../usuario/login.php');
    exit;
}

$error = "";
$success = "";
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $titulo = trim($_POST['titulo'] ?? '');
    $descripcion = trim($_POST['descripcion'] ?? '');
    $limite = (int) ($_POST['tiempo_limite'] ?? 0);
    $password = $_POST['password'] ?? '';

    $modo = 'concurso';

    if (empty($titulo) || empty($password)) {
        $error = "El título y la contraseña son obligatorios.";
    } else {
        $stmt = $conn->prepare("INSERT INTO examenes (titulo, descripcion, creador_id, tiempo_limite, password_examen, modo) VALUES (?, ?, ?, ?, ?, ?)");
        if ($stmt->execute([$titulo, $descripcion, $_SESSION['usuarioid'], $limite, $password, $modo])) {
            $success = "Concurso creado correctamente. Código: " . $conn->lastInsertId();
        } else {
            $error = "Error al crear el concurso.";
        }
    }
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Crear Concurso | Cuestionario Math</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            background: linear-gradient(115deg, #1e0843 30%, #060e2a 100%);
            min-height:100vh;margin:0;
            font-family: 'Segoe UI', Arial, sans-serif; color:#faffd7;
            display:flex; align-items:center; justify-content:center;
        }
        .panel-crear {
            background: rgba(40,13,44,0.97);
            border:2.2px solid #ffbb22;
            border-radius:20px;
            box-shadow:0 8px 38px #ffe66d44, 0 0 14px #ffc23455 inset;
            padding:39px 28px 29px 28px; width:98vw; max-width:410px;
            display:flex; flex-direction:column; align-items:center;
        }
        h1 { color: #ffbb22; text-shadow: 0 0 13px #ffbb22a4;}
        label { color:#ffe066; font-weight: 600;margin-top:13px;}
        input, textarea {
            width:100%;padding:10px 8px; margin-top:2px;
            font-size:1.07em; border-radius:10px;
            background:rgba(38,29,13,0.97); border:1.3px solid #fdc643;
            color:#fdeeb5; margin-bottom:14px; outline:none;
        }
        input:focus, textarea:focus {border-color:#ffbb22;box-shadow:0 0 8px #ffbb22a6;}
        .btn-crear {
            background: linear-gradient(90deg,#ffc234 60%,#ffbb22 100%);
            color: #1a2639; font-weight:700; font-size:1.09em;
            border:none; border-radius:12px;
            margin:17px 0 0 0; padding:12px 0; cursor:pointer;
            box-shadow:0 2px 13px #ffc23455;transition:background 0.21s;
        }
        .btn-crear:hover {background:linear-gradient(90deg,#ffbb22 80%,#ffc234 100%);}
        .error, .success {
            padding:8px 15px; border-radius:7px;
            margin-bottom:10px;text-align:center;font-weight:600;
        }
        .error {background:#a5221fdd;color:#ffe5d0;border:1px solid #ff232277;}
        .success {background:#1c155899;color:#fff1a3;border:1px solid #ffeb5077;}
        .enlace {margin-top:12px;text-align:center;}
        .enlace a {color:#ffc234;text-decoration:none;font-weight:600;}
        .enlace a:hover {color:#ffbb22;}
    </style>
</head>
<body>
<div class="panel-crear">
    <h1>Crear Concurso</h1>
    <?php if (!empty($error)): ?><div class="error"><?php echo htmlspecialchars($error); ?></div><?php endif; ?>
    <?php if (!empty($success)): ?><div class="success"><?php echo htmlspecialchars($success); ?></div><?php endif; ?>
    <form method="POST">
        <label for="titulo">Título</label>
        <input type="text" name="titulo" id="titulo" maxlength="255" required>

        <label for="descripcion">Descripción (opcional)</label>
        <textarea name="descripcion" id="descripcion" maxlength="1000" rows="2"></textarea>

        <label for="tiempo_limite">Tiempo límite en minutos (opcional)</label>
        <input type="number" name="tiempo_limite" id="tiempo_limite" min="0" placeholder="Ej: 15">

        <label for="password">Contraseña del concurso</label>
        <input type="password" name="password" id="password" required>

        <button class="btn-crear" type="submit">Crear Concurso</button>
    </form>
    <div class="enlace">
        <a href="../index.php">Volver al menú principal</a>
    </div>
</div>
</body>
</html>
