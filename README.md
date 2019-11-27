### Mendapatkan aplikasi FINAMA
- Clone aplikasi FINAMA dari github dengan mengetik git clone https://github.com/futsuunohito/FINAMA.git di terminal atau command prompt
- Jika tidak ada git, unduh file zip aplikasi FINAMA di https://github.com/futsuunohito/FINAMA
### Memasang dependencies dan aktivasi virtual environment
- Dengan menggunakan Python 3.6 atau Python 3.7, pasang beberapa dependencies FINAMA pada virtual environment baru. 
- Untuk membuat virtual  environment, lakukan hal-hal berikut
    - pip install virtual_env
    - virtual_env env_FINAMA
- Lakukan aktivasi virtual environment dengan cara berikut.
  - Jika sistem operasi pengguna adalah Linux
    - Buka terminal di folder FINAMA/virtual_env/
    - Ketik source bin/activate
  - Jika sistem operasi pengguna adalah Windows / Mac
    - Buat Python virtual environment baru di direktori manapun
    - Install dependencies sesuai dengan instruksi dibawah
    - Untuk mengaktifkan virtual environment, ketik env_FINAMA/Scripts/activate
- Adapun dependencies yang harus dipasang adalah sebagai berikut.
  - pip install mysqlclient
  - pip install django-widget-tweaks
  - pip install django-typeahead
### Serve Project
- Buka terminal atau command prompt di folder FINAMA/virtual_env/FINAMA
- Ketik python manage.py runserver
- Buka 127.0.0.1:8000 di browser
### Deaktivasi Virtual Env
- Jika sudah tidak digunakan, ketik deactivate di terminal atau command prompt untuk menutup virtual environment.
