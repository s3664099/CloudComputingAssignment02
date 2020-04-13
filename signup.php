<?php

    session_start();

    require 'vendor/autoload.php';
    use \Google\Cloud\Datastore\DatastoreClient;
    $datastore = new DatastoreClient(['projectId' => 'map-cc-assignment']);

    if ($_POST) {
        $email = $_POST['email'];
        $firstName = $_POST['firstname'];
        $surname = $_POST['surname'];
        $password = $_POST['password'];
        $confirm = $_POST['confirmpassword'];

        $emailErr = $firstNameErr = $surnameErr = $passwordErr = "";
        $error = FALSE;

        // Errors.
        if (empty($email)) {
            $emailErr = "Please enter an email.";
            $error = TRUE;
        }

        if (empty($firstName)) {
            $firstNameErr = "Please enter a first name.";
            $error = TRUE;
        }

        if (empty($surname)) {
            $surnameErr = "Please enter a surname.";
            $error = TRUE;
        }

        if (empty($password)|| empty($confirm)) {
            $passwordErr = "Please enter a password.";
            $error = TRUE;
        }

        if ($password != $confirm) {
            $passwordErr = "Passwords do not match.";
            $error = TRUE;
        }

        if ($error == FALSE) {
            $key = $datastore->key('User', $email);
            $user = $datastore->entity($key, ['firstName' => $firstName, 'surname' => $surname, 'password' =>  $password]);

            $datastore->insert($user);

            echo "Details correct. User created.";
        }
    }
    
?>


<html>
<body>
    <div>
    <form action="signup.php" method="post">
        <span><?php echo $emailErr;?></span><br>
        <label>Email:</label><br>
        <input type="text" name="email"><br>

        <span><?php echo $firstNameErr;?></span><br>
        <label>First Name:</label><br>
        <input type="text" name="firstname"><br>

        <span><?php echo $surnameErr;?></span><br>
        <label>Surname:</label><br>
        <input type="text" name="surname"><br>

        <span><?php echo $passwordErr?></span><br>
        <label>Password:</label><br>
        <input type="password" name="password"><br>
        <label>Confirm Password:</label><br>
        <input type="password" name="confirmpassword"><br>

        <input type="submit" value="Create Account">
    </form>
    
    </div>
</body>

</html>
