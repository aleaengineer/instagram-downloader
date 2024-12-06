from flask import Flask, render_template, request, jsonify
import instaloader
import os

app = Flask(__name__)
app.config["DOWNLOAD_FOLDER"] = "downloads"

# Membuat instance Instaloader
L = instaloader.Instaloader()

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    data = request.get_json()
    username_target = data.get("username_target")
    
    # Buat folder khusus untuk username target
    target_folder = os.path.join(app.config["DOWNLOAD_FOLDER"], username_target)
    os.makedirs(target_folder, exist_ok=True)
    
    # Ubah direktori kerja ke folder target
    original_directory = os.getcwd()
    os.chdir(target_folder)
    
    try:
        # Unduh konten profil
        L.login('tiyassaputrii', '@Koplok12!!')
        L.download_profile(username_target, profile_pic=False, fast_update=True)

        # Kembalikan direktori asli
        os.chdir(original_directory)
        return jsonify({"status": "success", "message": f"Konten dari @{username_target} berhasil diunduh."})
    except Exception as e:
        os.chdir(original_directory)  # Pastikan kembali ke direktori asli jika terjadi error
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
