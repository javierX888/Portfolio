from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from src.auth.forms import LoginForm, RegistrationForm
from src.auth.profile_form import ProfileForm
from src.models import User, db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('tasks.index'))  # Cambia a tu home

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('tasks.index'))  # Cambia a tu home
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
    return render_template('auth/login.html', form=form)

@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if current_user.is_authenticated:
        return redirect(url_for('tasks.index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('¡Cuenta creada correctamente! Ya puedes iniciar sesión.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión correctamente', 'success')
    return redirect(url_for('auth.login'))

@auth_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    
    if form.validate_on_submit():
        try:
            current_user.full_name = form.full_name.data
            
            # Manejar la foto de perfil
            if form.profile_picture_file.data:
                # Si se subió un archivo, convertirlo a base64
                import base64
                from PIL import Image
                import io
                
                file = form.profile_picture_file.data
                
                try:
                    # Abrir la imagen con PIL
                    img = Image.open(file)
                    
                    # Convertir a RGB si es necesario
                    if img.mode in ('RGBA', 'P', 'LA'):
                        img = img.convert('RGB')
                    
                    # Redimensionar si es muy grande (máximo 800x800)
                    max_size = 800
                    if img.width > max_size or img.height > max_size:
                        img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
                    
                    # Guardar en un buffer con compresión
                    buffer = io.BytesIO()
                    img.save(buffer, format='JPEG', quality=85, optimize=True)
                    file_data = buffer.getvalue()
                    
                    # Verificar tamaño final (máximo 400KB)
                    if len(file_data) > 400 * 1024:
                        # Comprimir más si es necesario
                        buffer = io.BytesIO()
                        img.save(buffer, format='JPEG', quality=70, optimize=True)
                        file_data = buffer.getvalue()
                        
                        if len(file_data) > 400 * 1024:
                            flash('La imagen es muy grande incluso después de comprimirla. Por favor usa una imagen más pequeña.', 'warning')
                            return redirect(url_for('auth.profile'))
                    
                    # Convertir a base64
                    base64_data = base64.b64encode(file_data).decode('utf-8')
                    current_user.profile_picture = f'data:image/jpeg;base64,{base64_data}'
                    
                except Exception as e:
                    flash(f'Error al procesar la imagen: {str(e)}. Intenta con otra imagen.', 'danger')
                    return redirect(url_for('auth.profile'))
                
            elif form.profile_picture.data:
                # Si se ingresó una URL, usarla
                url = form.profile_picture.data.strip()
                if url:
                    current_user.profile_picture = url
            
            db.session.commit()
            flash('¡Perfil actualizado correctamente!', 'success')
            return redirect(url_for('auth.profile'))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar el perfil: {str(e)}', 'danger')
            return redirect(url_for('auth.profile'))
    
    # Pre-llenar el formulario con los datos actuales
    if request.method == 'GET':
        form.full_name.data = current_user.full_name
        # Solo mostrar URL si no es base64
        if current_user.profile_picture and not current_user.profile_picture.startswith('data:'):
            form.profile_picture.data = current_user.profile_picture
    
    return render_template('auth/profile.html', form=form)