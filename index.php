<?php

echo "<h1>Hello! Welcome to Cloud Computing Assignment 2!</h1>";
?>

<html>
    <body>
        <div>
        <form action="auth.php" method="post">
            <label>Username:</label><br>
            <input type="text" name="username"><br>
            <label>Password:</label><br>
            <input type="password" name="password"><br>
            <input type="submit" value="Sign In">
        </form>
        </div>
            <h3>Don't have an account yet? Sign up here!</h3>
            <form action="signup.php"><input type="submit" value="Sign Up"></form>
        <div>
        
        </div>
    </body>
</html>
