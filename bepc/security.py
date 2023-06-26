import frappe

BENCH_PATH = frappe.utils.get_bench_path()

def execute():
    add_login_html_overrides()
    # add_login_js_overrides()
    add_file_overrides()
    comment_return_filepath()
    add_line_commentjs()
    comment_line_commentjs()
    # add_line_authpy()
    # modify_line_authpy()
    # add_line_authpy2()
    create_new_field()
    modify_user_profile_sidebar_html()
    modify_workspace_py()
    modify_user_py()
    modify_handler_py()
    workspace_js()
   
    

# frappe/frappe/www/login.html change content 
def add_login_html_overrides():
    file_path = "{}/{}".format(BENCH_PATH,
                               "apps/frappe/frappe/www/login.html")
    with open(file_path, "r") as file:
        content = file.read()

    updated_content = content.replace('autocomplete="current-password"', 'onpaste="return false;"\tautocomplete="off"')

    with open(file_path) as f:
        if 'onpaste="return false;"\tautocomplete="off"' in f.read():
            return

    with open(file_path, "w") as file:
        file.write(updated_content)
        print("frappe/frappe/www/login.html modified onpaste='return false;' & autocomplete='off'.")

    # code_to_append = '\n<script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js" integrity="sha512-E8QSvWZ0eCLGk4km3hxSsNmGWbLtSCSUcewDQPQWZF6pEU8GlT8a5fF32wOl1i8ftdMhssTrF/OhyGWwonTcXA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>'
    code_to_append = '/n<script src="https://cdnjs.cloudflare.com/ajax/libs/forge/0.10.0/forge.min.js"></script>'

    # Read the file content
    with open(file_path, 'r') as file:
        content = file.readlines()

    found_block_script = False

    with open(file_path) as f:
        if code_to_append in f.read():
            return

    # Search for {% block script %} and append the code if it's not already present
    for i, line in enumerate(content):
        if '{% block script %}' in line:
            found_block_script = True
            if code_to_append not in content[i+1]:
                content[i] = line.rstrip('\r\n')  # Remove trailing newline characters
                content.insert(i+1, code_to_append + '\n')  # Insert the code below {% block script %}
                with open(file_path, 'w') as file:
                    file.writelines(content)
                print("Code appended successfully.")
            # else:
            #     print("Code is already present in the file.")
            break

    # if not found_block_script:
    #     print("{% block script %} not found in the file.")


def add_login_js_overrides():
    file_path = "{}/{}".format(BENCH_PATH,
                                "apps/frappe/frappe/templates/includes/login/login.js")
    with open(file_path, "r") as file:
        lines = file.readlines()
        
    target_line1 = '$(".form-login").on("submit", function (event) {'
    new_line1 = """\t\t$.ajax({url: "http://localhost:8000/api/method/bepc.rsa-algo.rsa_gen_key", success: function(result){\n"""

    target_line2 = 'args.usr = frappe.utils.xss_sanitise(($("#login_email").val() || "").trim());'    
    new_line2 ="""\t\tconst publicKey = result.message['public_key_pem_date']\n\t\tfunction encryptWithRSA(plaintext) {\n\t\t\tconst publicKeyObj = forge.pki.publicKeyFromPem(publicKey);\n\t\t\tconst encrypted = publicKeyObj.encrypt(plaintext, 'RSA-OAEP', {\n\t\t\t\tmd: forge.md.sha256.create()\t\t\t\n\t\t\t});\n\t\t\treturn forge.util.encode64(encrypted);\n\t\t}\n\t\tconst plaintext = args.pwd;\n\t\tconst encryptedData = encryptWithRSA(plaintext).toString("base64");\n\t\targs.pwd = encryptedData\n\t\targs.no=result.message['rsa_no']\n"""

    target_line3 = """frappe.msgprint('{{ _("Both login and password required") }}');"""
    new_line3 = "});\n"

    new_line4 = "\t}"

    with open(file_path) as f:
        if '\t\t$.ajax({url: "http://localhost:8000/api/method/bepc.rsa-algo.rsa_gen_key", success: function(result){\n' in f.read():
            return

    # if existing1 not in lines:
    index = -1
    for i, line in enumerate(lines):
        if target_line1 in line:
            index = i
            break

    if index != -1:
        lines.insert(index + 2, new_line1)
      
    index2 = -1
    for i, line in enumerate(lines):
        if target_line2 in line:
            index2 = i
            break
    if index2 != -1:
        lines.insert(index2 + 2, new_line2)

    index4 = -1
    for i, line in enumerate(lines):
        if target_line3 in line:
            index4 = i
            break
    if index4 != -1:
        lines.insert(index4 + 5, new_line4)
    
    with open(file_path) as f:
        if "const publicKey = result.message['public_key_pem_date']" in f.read():
            return 
        
    index3 = -1
    for i, line in enumerate(lines):
        if target_line3 in line:
            index3 = i
            break
    if index3 != -1:
        lines.insert(index3 + 6, new_line3)
    
    with open(file_path) as f:
        if "const publicKey = result.message['public_key_pem_date']" in f.read():
            return 
        
    with open(file_path, "w") as file:
        file.writelines(lines)
        print("frappe/frappe/templates/includes/login/login.js modified with new line.")

    
    with open(file_path, "r") as file:
        content = file.read()

    updated_content = content.replace("""404: get_error_handler('{{ _("User does not exist.")}}')""", """404: get_error_handler('{{ _("Email Sent.")}}')""")

    with open(file_path) as f:
        if """404: get_error_handler('{{ _("Email Sent.")}}')""" in f.read():
            return

    with open(file_path, "w") as file:
        file.write(updated_content)
        print("""frappe/frappe/templates/includes/login/login.js modified 404: get_error_handler('{{ _("Email Sent.")}}').""")

def add_file_overrides():
    file_path = "{}/{}".format(BENCH_PATH,
                                "apps/frappe/frappe/core/doctype/file/file.py")
    with open(file_path, "r") as file:
        lines = file.readlines()

    target_line1 = 'def set_file_name(self):'
    new_line1 = '\t\tif has_multiple_extensions(self.file_name):\n\t\t\tfrappe.throw("File contains more than one extension.")\n\n'
    
    target_line2 = 'def write_file(self):'
    new_line2 = '\t\tfile_path1 = file_path\n\t\tfile_type = check_file_type(file_path1)\n\t\tif file_type is not None:\n\t\t\treturn file_path1\n\t\t# Perform further actions or checks for the specific file type\n\t\telse:\n\t\t\tfrappe.throw("Invalid file type.")\n\n'
    
    existing1 = '\t\tif has_multiple_extensions(self.file_name):\n'
    existing2 = '\t\tfile_path1 = file_path\n'

    with open(file_path) as f:
        if 'if has_multiple_extensions(self.file_name):' in f.read():
            return
    # add new line on def set_file_name(self) method
    # if existing1 not in lines:
    index = -1
    for i, line in enumerate(lines):
        if target_line1 in line:
            index = i
            break
    if index != -1:
        lines.insert(index + 6, new_line1)
    
    with open(file_path) as f:
        if 'file_path1 = file_path' in f.read():
            return
    # add new line on def write_file(self) method
    # if existing2 not in lines:
    index2 = -1
    for i, line in enumerate(lines):
        if target_line2 in line:
            index2 = i
            break
    if index2 != -1:
        lines.insert(index2 + 17, new_line2)

    with open(file_path, "w") as file:
        file.writelines(lines)

    with open(file_path) as f:
        if 'allowed_mime_types = {' in f.read():
            return
    
    with open(file_path, "a+") as f:   
        f.write(
    "\nallowed_mime_types = {\n\
        'image': ['image/jpeg', 'image/png', 'image/gif'],\n\
        'document': ['application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'],\n\
        'pdf': ['application/pdf'],\n\
        'video': ['video/mp4', 'video/quicktime', 'video/x-msvideo', 'video/x-ms-wmv', 'video/x-matroska'],\n\
        'excel' : ['application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'application/vnd.ms-excel.sheet.macroEnabled.12', 'application/vnd.openxmlformats-', 'application/vnd.ms-excel.template.macroEnabled.12']\n\
        }\n\
    \ndef check_file_type(file_path):\n\
    mime_type, _ = mimetypes.guess_type(file_path)\n\
    if mime_type is not None:\n\
        for file_type, allowed_types in allowed_mime_types.items():\n\
            if mime_type in allowed_types:\n\
                return file_type\n\
    return None\n\
    \ndef has_multiple_extensions(filename):\n\
        base_name, extension = os.path.splitext(filename)\n\
        second_extension = os.path.splitext(base_name)[1]\n\
        return bool(second_extension)\n")
            
        print("frappe/frappe/core/doctype/file/file.py modified with new lines.")

# Comment return file_path in file.py on def write_file(self) method
def comment_return_filepath():
    file_path = "{}/{}".format(BENCH_PATH,
                                "apps/frappe/frappe/core/doctype/file/file.py")
    with open(file_path, "r") as file:
        lines = file.readlines()

    method_name= "def write_file(self):"
    line_to_comment= "return file_path"

    # Checked '#\t\treturn file_path' exist in the file.py
    with open(file_path) as f:
        if '# \t\treturn file_path' in f.read():
            return

    with open(file_path, 'w') as file:
        in_target_method = False
        for line in lines:
            if method_name in line:
                in_target_method = True
            elif line.strip().startswith('def '):
                in_target_method = False

            if in_target_method and line.strip() == line_to_comment:
                # Comment the line
                line = '# ' + line

            file.write(line)
        print("frappe/frappe/core/doctype/file/file.py commented return file_path")

def add_line_commentjs():
    file_path = "{}/{}".format(BENCH_PATH,
                                "apps/frappe/frappe/public/js/frappe/form/controls/comment.js")
    
    with open(file_path, "r") as file:
        lines = file.readlines()

    target_line1 = 'submit() {'
    new_line1 = '\t\tif (this.on_submit) {\n\t\t\tvar value = this.get_value();\n\t\t\tvar sanitizedValue = sanitizeHtml(value);\n\t\t\tthis.on_submit(sanitizedValue);\n\t\t}\n\t\tfunction sanitizeHtml(value) {\n\t\t\tvar sanitizedValue = value.replace(/<\/?[^>]+(>|$)/g, '');\n\t\t\treturn sanitizedValue.trim();\n\t\t}\n'

    # Checked '\t\tif (this.on_submit) {' exist in the comment.js
    with open(file_path) as f:
        if '\t\tif (this.on_submit) {' in f.read():
            return

    # add new line on 'submit() {' method
    index = -1
    for i, line in enumerate(lines):
        if target_line1 in line:
            index = i
            break
    if index != -1:
        lines.insert(index + 2, new_line1)
    
    with open(file_path, "w") as file:
        file.writelines(lines)
        print("frappe/frappe/public/js/frappe/form/controls/comment.js modified with new lines.")

# Comment 'this.on_submit && this.on_submit(this.get_value());' in comment.js on 'submit() {' method
def comment_line_commentjs():
    file_path = "{}/{}".format(BENCH_PATH,
                                "apps/frappe/frappe/public/js/frappe/form/controls/comment.js")
    
    with open(file_path, "r") as file:
        lines = file.readlines()

    method_name= "submit() {"
    line_to_comment= "this.on_submit && this.on_submit(this.get_value());"

    # Checked '// \t\tthis.on_submit && this.on_submit(this.get_value());' exist in the comment.js
    with open(file_path) as f:
        if '// \t\tthis.on_submit && this.on_submit(this.get_value());' in f.read():
            return

    with open(file_path, 'w') as file:
        in_target_method = False
        for line in lines:
            if method_name in line:
                in_target_method = True
            elif line.strip().startswith('def '):
                in_target_method = False

            if in_target_method and line.strip() == line_to_comment:
                # Comment the line
                line = '// ' + line

            file.write(line)
        print("frappe/frappe/public/js/frappe/form/controls/comment.js commented this.on_submit && this.on_submit(this.get_value());")

def add_line_authpy():
    file_path = "{}/{}".format(BENCH_PATH,
                                "apps/frappe/frappe/auth.py")
    with open(file_path, "r") as file:
        lines = file.readlines()
        
    target_line1 = 'def authenticate(self, user: str = None, pwd: str = None):'
    new_line1 = """\t\tras_data=frappe.db.sql("select private_key_pem_date from `rsa_data` where name='%s' AND flag='1' "%(frappe.form_dict.get('no')),as_dict=True)\n\t\tif ras_data:\n\n\t\t\tfrappe.db.sql("Update `rsa_data` set flag='0' where name='%s' "%(frappe.form_dict.get('no')))\n\t\t\timport base64\n\t\t\tfrom cryptography.hazmat.primitives import serialization\n\t\t\tfrom cryptography.hazmat.primitives.asymmetric import rsa\n\t\t\tfrom cryptography.hazmat.primitives import hashes\n\t\t\tfrom cryptography.hazmat.primitives.asymmetric import padding\n\t\t\tprivate_key_pem=ras_data[0]['private_key_pem_date']\n\t\t\t#put the encrypted data received from the client side\n\t\t\tencrypted_data_base64 = frappe.form_dict.get("pwd")\n\n\t\t\tencrypted_data = base64.b64decode(encrypted_data_base64) # here it is converted into binary\n\t\t\t# creating the loaded private key\n\t\t\tloaded_private_key = serialization.load_pem_private_key(\n\t\t\t\tprivate_key_pem.encode(),\n\t\t\t\tpassword=None\n\t\t\t)\n\t\t\t# decoding\n\t\t\tdecrypted_data = loaded_private_key.decrypt(\n\t\t\t\tencrypted_data,\n\t\t\t\tpadding.OAEP(\n\t\t\t\t\tmgf=padding.MGF1(algorithm=hashes.SHA256()),\n\t\t\t\t\talgorithm=hashes.SHA256(),\n\t\t\t\t\tlabel=None\n\t\t\t\t)\n\t\t\t)\n\t\t\t# Print the decrypted data\n\t\t\tpassword=decrypted_data.decode()\n\t\t\t##################################### end of my code\n"""
    

    # existing1='from Crypto.Cipher import AES'
    # existing2 = 'user, pwd = frappe.form_dict.get("usr")'

    with open(file_path) as f:
        if 'ras_data=frappe.db.sql("select private_key_pem_date from `rsa_data` where name=' in f.read():
            return 

    index = -1
    for i, line in enumerate(lines):
        if target_line1 in line:
            index = i
            break

    if index != -1:
        lines.insert(index + 1, new_line1)
       

    with open(file_path, "w") as file:
        file.writelines(lines)
        print("auth.line modified with new line1")

def modify_line_authpy():
    file_path = "{}/{}".format(BENCH_PATH,
                                "apps/frappe/frappe/auth.py")
    with open(file_path, "r") as file:
        lines = file.readlines()

    updated_content = []
    replace_start_line = 261
    replace_end_line = 288

    new_code = [
            '\tfrom frappe.core.doctype.user.user import User\n',

			'\tif not (user and pwd):\n',
				'\t\tuser, pwd = frappe.form_dict.get("usr"), password\n',
			'\tif not (user and pwd):\n',
				'\t\tself.fail(_("Incomplete login details"), user=user)\n',

			'\tuser = User.find_by_credentials(user, pwd)\n',

			'\tif not user:\n',
				'\t\tself.fail("Invalid login credentials")\n',

        '# Current login flow uses cached credentials for authentication while checking OTP.\n',
		'# Incase of OTP check, tracker for auth needs to be disabled(If not, it can remove tracker history as it is going to succeed anyway)\n',
		'# Tracker is activated for 2FA incase of OTP.\n',
			'\tignore_tracker = should_run_2fa(user.name) and ("otp" in frappe.form_dict)\n',
			'\ttracker = None if ignore_tracker else get_login_attempt_tracker(user.name)\n',
			'\tif not user.is_authenticated:\n',
				'\t\ttracker and tracker.add_failure_attempt()\n',
				'\t\tself.fail("Invalid login credentials", user=user.name)\n',
			'\telif not (user.name == "Administrator" or user.enabled):\n',
				'\t\ttracker and tracker.add_failure_attempt()\n',
				'\t\tself.fail("User disabled or missing", user=user.name)\n',
			'\telse:\n',
				'\t\ttracker and tracker.add_success_attempt()\n',
			'\tself.user = user.name\n',

    ]

    for i, line in enumerate(lines, start=1):
        if replace_start_line <= i <= replace_end_line:
            if i == replace_start_line:
                indentation = line[:len(line) - len(line.lstrip())]
                updated_content.extend(indentation + code_line for code_line in new_code)
            else:
                continue
        else:
            updated_content.append(line)

    with open(file_path) as f:
        if 'user, pwd = frappe.form_dict.get("usr"), password' in f.read():
            return

    with open(file_path, "w") as file:
        file.writelines(updated_content)
        print("/apps/frappe/frappe/core/auth.py modified")

def add_line_authpy2():
    file_path = "{}/{}".format(BENCH_PATH,
                                "apps/frappe/frappe/auth.py")
    with open(file_path, "r") as file:
        lines = file.readlines()
        
    target_line1 = 'self.user = user.name'
    new_line1 ='\t\telse:\n\t\t\tfrappe.throw("Bad Credentials Contact To Administrator")\n'

    with open(file_path) as f:
        if 'frappe.throw("Bad Credentials Contact To Administrator")' in f.read():
            return 

    index = -1
    for i, line in enumerate(lines):
        if target_line1 in line:
            index = i
            break

    if index != -1:
        lines.insert(index + 1, new_line1)
       

    with open(file_path, "w") as file:
        file.writelines(lines)
        print("auth.line modified with new line2")
    
        
def create_new_field():
        confirm_password_data=frappe.get_all("DocField",{"parent":"User","fieldname":"confirm__password"},['name','idx'])
        if not confirm_password_data:
            confirm_password_data=frappe.get_all("DocField",{"parent":"User","fieldname":"new_password"},['name','idx'])
            idx_no=confirm_password_data[0]['idx']
            other_idx=frappe.get_all("DocField",filters=[["parent",'=',"User"],["idx",">",idx_no]],fields=['name','idx'],
                order_by="idx asc")
            for t in other_idx:
                frappe.db.sql(""" UPDATE `tabDocField` SET idx=%s where name='%s' """%(t['idx']+1,t['name']))
            data=frappe.get_doc("DocType","User")
            data.append("fields",{
                'label':"Confirm Password",
                "fieldtype":"Password",
                "fieldname":"confirm__password",
                "idx":idx_no+1
            })
            data.save()
            
def modify_user_profile_sidebar_html():
    file_path = "{}/{}".format(BENCH_PATH, "apps/frappe/frappe/desk/page/user_profile/user_profile_sidebar.html")
    with open(file_path, "r") as file:
        content = file.readlines()

    updated_content = []
    for i, line in enumerate(content, start=1):
        if i == 51 and '<p><a class="edit-profile-link">{%=__("Edit Profile") %}</a></p>' in line:
            updated_content.append("<!--" + line.strip() + "-->\n")
        else:
            updated_content.append(line)
            
    with open(file_path) as f:
        if '<!--<p><a class="edit-profile-link">{%=__("Edit Profile") %}</a></p>-->' in f.read():
            return

    with open(file_path, "w") as file:
        file.writelines(updated_content)
        print("frappe/frappe/desk/page/user_profile/user_profile_sidebar.html modified. 'Edit Profile' line at line 51 commented.")
        
def modify_workspace_py():
    file_path = "{}/{}".format(BENCH_PATH, "apps/frappe/frappe/desk/doctype/workspace/workspace.py")
    with open(file_path, "a") as file:
        method_code = '''\n@frappe.whitelist()\ndef get_user_role():\n\tuser_role = frappe.db.get_value("User", {"name": frappe.session.user}, ["name"])\n\treturn user_role\n'''
        
        with open(file_path) as f:
            if 'def get_user_role():' in f.read():
                return
        
        file.write(method_code)
    
    print("frappe/frappe/desk/doctype/workspace/workspace.py modified. 'get_user_role' method added.")
        

def modify_user_py():
    file_path = "{}/{}".format(BENCH_PATH, "apps/frappe/frappe/core/doctype/user/user.py")
    with open(file_path, "r") as file:
        content = file.readlines()
        
    target_line1 = 'def validate(self):'
    new_line1 = """\t\t\tself.confirm__password=None\n"""
    
    with open(file_path) as f:
        if '\t\tif(args.cmd != "login")\n' in f.read():
            return
    
    index = -1
    for i, line in enumerate(content):
        if target_line1 in line:
            index = i
            break
        
    if index != -1:
        content.insert(index + 7, new_line1)
        
    with open(file_path) as f:
            if 'self.confirm__password=None' in f.read():
                return
        
    with open(file_path, "w") as file:
        file.writelines(content)
        print("user.py modified with new lines.")

    updated_content = []
    replace_start_line = 545
    replace_end_line = 556

    new_code = [
        '"""test password strength"""\n',
        'if self.flags.ignore_password_policy:\n',
        '\treturn\n',
        'if self.__new_password:\n',
        '\tif self.confirm__password == self.__new_password:\n',
        '\t\tuser_data = (self.first_name, self.middle_name, self.last_name, self.email, self.birth_date)\n',
        '\t\tresult = test_password_strength(self.__new_password, "", None, user_data)\n',
        '\t\tfeedback = result.get("feedback", None)\n',
        '\t\tif feedback and not feedback.get("password_policy_validation_passed", False):\n',
        '\t\t\thandle_password_test_fail(feedback)\n',
        '\telse:\n',
        '\t\tfrappe.throw("New Password is not matching with Confirm Password")\n\n'
    ]

    for i, line in enumerate(content, start=1):
        if replace_start_line <= i <= replace_end_line:
            if i == replace_start_line:
                indentation = line[:len(line) - len(line.lstrip())]
                updated_content.extend(indentation + code_line for code_line in new_code)
            else:
                continue
        else:
            updated_content.append(line)

    with open(file_path) as f:
        if 'if self.confirm__password == self.__new_password:' in f.read():
            return

    with open(file_path, "w") as file:
        file.writelines(updated_content)
        print("/apps/frappe/frappe/core/doctype/user/user.py modified. 'password_strength_test' method replaced.")


def modify_handler_py():
    file_path = "{}/{}".format(BENCH_PATH, "apps/frappe/frappe/handler.py")
    with open(file_path, "r") as file:
        content = file.readlines()

    updated_content = []
    replace_line_number = 74

    for i, line in enumerate(content, start=1):
        if i == replace_line_number:
            updated_content.append('\t\tfrappe.throw("Invalid Parameter")\n')
        else:
            updated_content.append(line)
            
    with open(file_path) as f:
        if """frappe.throw("Invalid Parameter""" in f.read():
            return

    with open(file_path, "w") as file:
        file.writelines(updated_content)
        print("/apps/frappe/frappe/handler.py modified. Line 74 replaced.")



def workspace_js():
    file_path = "{}/{}".format(BENCH_PATH, "apps/frappe/frappe/public/js/frappe/views/workspace/workspace.js")
    with open(file_path, "r") as file:
        content = file.readlines()
        
    target_line1 = 'frappe.workspace.show();'
    new_line1 = """\tvar flag=0\n\tfrappe.call({\n\t\tmethod:"frappe.desk.doctype.workspace.workspace.get_user_role",\n\t\targs: {\n\t\t\tpage: this.page\n\t\t},\n\t\tcallback: function(r){\n\t\t\tvar result = r.message;\n\t\t\tflag=result\n\t\t}\n\t});\n"""
    
    with open(file_path) as f:
        if """method:"frappe.desk.doctype.workspace.workspace.get_user_role",""" in f.read():
            return
    
    index = -1
    for i, line in enumerate(content):
        if target_line1 in line:
            index = i
            break
        
    if index != -1:
        content.insert(index + 3, new_line1)
        
    with open(file_path, "w") as file:
        file.writelines(content)
        print("workspace.js modified with top lines.")
        
    target_line2 = 'this.make_blocks_sortable();'
    new_line2 = """\t\t if (flag=='Administrator'){\n"""
    
    with open(file_path) as f:
        if """if (flag=='Administrator'){""" in f.read():
            return
    
    index = -1
    for i, line in enumerate(content):
        if target_line2 in line:
            index = i
            break
        
    if index != -1:
        content.insert(index + 3, new_line2)
        
    with open(file_path, "w") as file:
        file.writelines(content)
        print("workspace.js modified with middle lines.")
        
    #####
       
    target_line3 = 'this.initialize_new_page();'
    new_line3 = """\t\t}else{\n\t\t\t$('.actions-btn-group').prop('hidden', true);\n\t\t}\n"""
    
    with open(file_path) as f:
        if """$('.actions-btn-group').prop('hidden', true);""" in f.read():
            return
    
    index = -1
    for i, line in enumerate(content):
        if target_line3 in line:
            index = i
            break
        
    if index != -1:
        content.insert(index + 2, new_line3)
        
    with open(file_path, "w") as file:
        file.writelines(content)
        print("workspace.js modified with end lines.")