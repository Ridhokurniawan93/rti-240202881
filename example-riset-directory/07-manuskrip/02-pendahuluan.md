# Pendahuluan

JWT banyak digunakan sebagai mekanisme autentikasi dan otorisasi pada arsitektur mikroservis. Validasi token JWT membutuhkan kunci publik yang dapat diambil dari JWKS berdasarkan header `kid`. Namun, proses resolusi `kid` ini dapat dieksploitasi oleh penyerang melalui serangan **JWKS Endpoint Flooding**.

Dalam serangan tersebut, gateway menerima permintaan token dengan `kid` acak atau tidak terdaftar. Jika setiap `kid` memicu lookup backend, beban database dan identitas service akan meningkat secara drastis, sehingga menurunkan ketersediaan layanan untuk pengguna sah.

Studi ini bertujuan untuk merancang dan mengevaluasi mekanisme mitigasi yang menggunakan Redis sebagai cache positif/negatif dan PostgreSQL sebagai source of truth serta counter rate limit. Penelitian membandingkan dua mode operasi: tanpa mitigasi (`none`) dan dengan mitigasi (`hybrid`), lalu mengevaluasi dampaknya terhadap performa dan beban resource.
