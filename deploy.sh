read -r -p 'Commit message: ' desc  # Perintah untuk memasukkan komentar dalam perubahan(Wajib di isi),
git add --all          		    # perubahan semua file,
git commit -m "$desc"               # Komentarnya,
git push origin master              # deploy ke git (origin).
