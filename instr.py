from PyQt5.QtCore import QTime


win_x, win_y = 200, 100
win_width, win_height = 1000, 600

txt_hello = 'Selamat datang di program deteksi status kesehatan!'
txt_next = 'Mulai'
txt_instruction = ('Aplikasi ini memungkinkan Anda menggunakan tes Rufier untuk melakukan diagnosis awal kesehatan Anda.\n'
                   'Tes Rufier adalah serangkaian latihan fisik yang dirancang untuk menilai kinerja jantung Anda selama aktivitas fisik.\n'
                   'Subjek berbaring telentang selama 5 menit dan mengukur denyut nadi selama 15 detik; \n'
                   'kemudian, dalam waktu 45 detik, subjek melakukan 30 kali jongkok.\n'
                   'Setelah latihan selesai, subjek berbaring kembali dan denyut nadinya diukur lagi selama 15 detik pertama \n'
                   'dan kemudian selama 15 detik terakhir dari menit pertama masa pemulihan.\n'
                   'Penting! Jika Anda merasa tidak sehat selama tes (pusing,\n'
                   'telinga berdenging, sesak napas, dll.), hentikan tes dan konsultasikan dengan dokter.')
txt_title = 'Kesehatan'
txt_name = 'Masukkan Nama Lengkap Anda:'
txt_hintname = "Nama Lengkap"
txt_hintage = "0"
txt_test1 = 'Berbaringlah telentang dan ukur denyut nadi Anda selama 15 detik. Klik tombol "Mulai tes pertama" untuk memulai timer.\nTuliskan hasilnya di kolom yang sesuai.'
txt_test2 = 'Lakukan 30 kali jongkok dalam 45 detik. Untuk itu, klik tombol "Mulai melakukan jongkok" \nuntuk memulai penghitung jongkok.'
txt_test3 = 'Berbaringlah telentang dan ukur denyut nadi Anda selama 15 detik pertama pada menit pertama, kemudian selama 15 detik terakhir pada menit pertama.\nTekan tombol "Mulai tes akhir" untuk memulai timer.\nDetik yang harus diukur ditandai dengan warna hijau dan menit yang tidak perlu diukur ditandai dengan warna hitam. Tuliskan hasilnya di kolom yang sesuai.'
txt_sendresults = 'Kirim hasil'
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_starttest1 = 'Mulai tes pertama'
txt_starttest2 = 'Mulai melakukan jongkok'
txt_starttest3 = 'Mulai tes akhir'
txt_timer = ''

txt_age = 'Umur penuh (tahun):'
txt_finalwin = 'Hasil'
txt_index = 'Indeks Rufier: '
txt_workheart = 'Kinerja jantung: '
time = QTime(0, 0, 15)
txt_timer = time.toString("hh:mm:ss")
txt_res1 = "low. See your doctor right away!"
txt_res2 = "satisfactory. See your doctor!"
txt_res3 = "average. It may be worth seeing your doctor to get checked out."
txt_res4 = "above average"
txt_res5 = "high"
