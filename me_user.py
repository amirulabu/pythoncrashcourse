from user import User, Admin, Privileges

me = User('amirul', 'abu', 26, 'Labuan')

me.describe_user()
me.greet_user()

print("Default login attempts: " + str(me.login_attempts))

me.increment_login_attempts()
me.increment_login_attempts()
print("After two times login attempts: " + str(me.login_attempts))

me.reset_login_attempts()
print("Reset login attempts: " + str(me.login_attempts))

me_admin = Admin('amirul', 'abu', 26, 'Labuan', 'can ban users')

me_admin.privileges.show_privileges()