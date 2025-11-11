<?php
session_start();
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $_SESSION['tmp_formula'] = [
        'enunciado' => $_POST['enunciado'] ?? '',
        'opciona' => $_POST['opA'] ?? '',
        'opcionb' => $_POST['opB'] ?? '',
        'opcionc' => $_POST['opC'] ?? '',
        'opcionsd' => $_POST['opD'] ?? '',
        'correcta' => $_POST['correcta'] ?? '',
    ];
    header('Location: crear_examen.php');
    exit;
}
$data = $_SESSION['tmp_formula'] ?? [
    'enunciado'=>'','opciona'=>'','opcionb'=>'','opcionc'=>'','opcionsd'=>'','correcta'=>''
];
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Editar Pregunta Matemática</title>
    <script src="https://unpkg.com/mathlive/dist/mathlive.min.js"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {background:#f8f9fd;font-family:'Inter',sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;}
        .panel-box {background:#fff;border-radius:14px;box-shadow:0 8px 60px #dbeafd99;padding:40px 35px;max-width:410px;width:100%;}
        h2 {color:#2562ec;text-align:center;}
        form {display:flex;flex-direction:column;gap:15px;}
        button {background:#2562ec;color:#fff;border:none;padding:10px;border-radius:8px;font-weight:700;cursor:pointer;}
        button:hover {background:#193278;}
        label {color:#2562ec;margin-bottom:2px;margin-top:7px;}
        select,input {font-size:1em;}
        math-field {width:100%;min-height:36px;border-radius:8px;border:1px solid #d0dbed;background:#f7f8fa;color:#222;font-size:1em;}
    </style>
</head>
<body>
    <div class="panel-box">
        <h2>Pregunta matemática</h2>
        <form method="post">
            <label>Enunciado:</label>
            <math-field name="enunciado" id="enunciado" virtual-keyboard-mode="onfocus"><?= htmlspecialchars($data['enunciado']) ?></math-field>
            <label>Opción A:</label>
            <math-field name="opA" id="opA" virtual-keyboard-mode="onfocus"><?= htmlspecialchars($data['opciona']) ?></math-field>
            <label>Opción B:</label>
            <math-field name="opB" id="opB" virtual-keyboard-mode="onfocus"><?= htmlspecialchars($data['opcionb']) ?></math-field>
            <label>Opción C:</label>
            <math-field name="opC" id="opC" virtual-keyboard-mode="onfocus"><?= htmlspecialchars($data['opcionc']) ?></math-field>
            <label>Opción D:</label>
            <math-field name="opD" id="opD" virtual-keyboard-mode="onfocus"><?= htmlspecialchars($data['opcionsd']) ?></math-field>
            <label>Respuesta correcta:</label>
            <select name="correcta" required>
                <option value="">Elige</option>
                <option value="a" <?= $data['correcta']=='a'?'selected':''; ?>>A</option>
                <option value="b" <?= $data['correcta']=='b'?'selected':''; ?>>B</option>
                <option value="c" <?= $data['correcta']=='c'?'selected':''; ?>>C</option>
                <option value="d" <?= $data['correcta']=='d'?'selected':''; ?>>D</option>
            </select>
            <button type="submit" onclick="
                document.querySelector('input[name=enunciado]').value=document.getElementById('enunciado').value;
                document.querySelector('input[name=opA]').value=document.getElementById('opA').value;
                document.querySelector('input[name=opB]').value=document.getElementById('opB').value;
                document.querySelector('input[name=opC]').value=document.getElementById('opC').value;
                document.querySelector('input[name=opD]').value=document.getElementById('opD').value;
            ">Guardar y volver</button>
        </form>
    </div>
</body>
</html>
