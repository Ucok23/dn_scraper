import unittest
from unittest.mock import patch, Mock
from src.dn_scraper import DetikNewsScraper


class TestDetikNewsScraper(unittest.TestCase):

    html = '''
        <div class="list-content">         

      
      
         <article class="list-content__item">
   <div class="media media--right media--image-radius block-link">
      <div class="media__image">
         <a href="https://finance.detik.com/berita-ekonomi-bisnis/d-7780373/buat-yang-suka-nyinyir-program-makan-bergizi-gratis-nih-jawaban-prabowo" dtr-evt="search result relevansi" dtr-sec="search result relevansi" dtr-act="artikel" onclick="_pt(this)" dtr-idx="1" dtr-id="7780373" dtr-ttl="Buat yang Suka Nyinyir Program Makan Bergizi Gratis, Nih Jawaban Prabowo" class="media__link" d-collected="7780373searchresultrelevansi">
            <span class="ratiobox ratiobox--4-3 lqd" style="background-image: url(&quot;https://akcdn.detik.net.id/visual/2025/02/10/presiden-prabowo-subianto_43.jpeg?w=250&amp;q=90&quot;);">
                 <img src="https://akcdn.detik.net.id/visual/2025/02/10/presiden-prabowo-subianto_43.jpeg?w=250&amp;q=90" alt="Buat yang Suka Nyinyir Program Makan Bergizi Gratis, Nih Jawaban Prabowo" title="Buat yang Suka Nyinyir Program Makan Bergizi Gratis, Nih Jawaban Prabowo" class="" style="display: none;">            </span>
         </a>
      </div>
      <div class="media__text">
         <h2 class="media__subtitle">
           detikFinance         </h2>
         <h3 class="media__title">
            <a href="https://finance.detik.com/berita-ekonomi-bisnis/d-7780373/buat-yang-suka-nyinyir-program-makan-bergizi-gratis-nih-jawaban-prabowo" dtr-evt="search result relevansi" dtr-sec="search result relevansi" dtr-act="artikel" onclick="_pt(this)" dtr-idx="1" dtr-id="7780373" dtr-ttl="Buat yang Suka Nyinyir Program Makan Bergizi Gratis, Nih Jawaban Prabowo" class="media__link">Buat yang Suka Nyinyir Program Makan Bergizi Gratis, Nih Jawaban Prabowo</a>
         </h3>
         <div class="media__desc">
            Presiden Prabowo Subianto merespons sindiran terhadap program Makan Bergizi Gratis (MBG).         </div>
         <div class="media__date">
            <span d-time="1739665798" title="Minggu, 16 Feb 2025 07:29 WIB">4 jam yang lalu</span>         </div>
      </div>
   </div>
</article>
         
               
         <article class="list-content__item">
   <div class="media media--right media--image-radius block-link">
      <div class="media__image">
         <a href="https://finance.detik.com/berita-ekonomi-bisnis/d-7777513/prabowo-sebut-makan-bergizi-gratis-investasi-sasar-330-ribu-sekolah" dtr-evt="search result relevansi" dtr-sec="search result relevansi" dtr-act="artikel" onclick="_pt(this)" dtr-idx="2" dtr-id="7777513" dtr-ttl="Prabowo Sebut Makan Bergizi Gratis Investasi, Sasar 330 Ribu Sekolah" class="media__link" d-collected="7777513searchresultrelevansi">
            <span class="ratiobox ratiobox--4-3 lqd" style="background-image: url(&quot;https://akcdn.detik.net.id/visual/2025/02/10/prabowo-saat-mengecek-makan-bergizi-gratis-di-sd-bogor-dok-istimewa-2_43.jpeg?w=250&amp;q=90&quot;);">
                 <img src="https://akcdn.detik.net.id/visual/2025/02/10/prabowo-saat-mengecek-makan-bergizi-gratis-di-sd-bogor-dok-istimewa-2_43.jpeg?w=250&amp;q=90" alt="Prabowo Sebut Makan Bergizi Gratis Investasi, Sasar 330 Ribu Sekolah" title="Prabowo Sebut Makan Bergizi Gratis Investasi, Sasar 330 Ribu Sekolah" class="" style="display: none;">            </span>
         </a>
      </div>
      <div class="media__text">
         <h2 class="media__subtitle">
           detikFinance         </h2>
         <h3 class="media__title">
            <a href="https://finance.detik.com/berita-ekonomi-bisnis/d-7777513/prabowo-sebut-makan-bergizi-gratis-investasi-sasar-330-ribu-sekolah" dtr-evt="search result relevansi" dtr-sec="search result relevansi" dtr-act="artikel" onclick="_pt(this)" dtr-idx="2" dtr-id="7777513" dtr-ttl="Prabowo Sebut Makan Bergizi Gratis Investasi, Sasar 330 Ribu Sekolah" class="media__link">Prabowo Sebut Makan Bergizi Gratis Investasi, Sasar 330 Ribu Sekolah</a>
         </h3>
         <div class="media__desc">
            Progam Makan Bergizi Gratis (MBG) merupakan kebijakan prioritas Presiden Prabowo Subianto. Menurut Prabowo, Program ini adalah investasi masa depan Indonesia.         </div>
         <div class="media__date">
            <span d-time="1739454298" title="Kamis, 13 Feb 2025 20:44 WIB">Kamis, 13 Feb 2025 20:44 WIB</span>         </div>
      </div>
   </div>
</article>
         
               
         <article class="list-content__item">
   <div class="media media--right media--image-radius block-link">
      <div class="media__image">
         <a href="https://health.detik.com/berita-detikhealth/d-7777235/bpom-siap-kawal-makan-bergizi-gratis-ini-tugas-utamanya" dtr-evt="search result relevansi" dtr-sec="search result relevansi" dtr-act="artikel" onclick="_pt(this)" dtr-idx="3" dtr-id="7777235" dtr-ttl="BPOM Siap Kawal Makan Bergizi Gratis, Ini Tugas Utamanya" class="media__link" d-collected="7777235searchresultrelevansi">
            <span class="ratiobox ratiobox--4-3 lqd" style="background-image: url(&quot;https://akcdn.detik.net.id/visual/2025/02/12/kepala-bpom-taruna-ikrar_43.jpeg?w=250&amp;q=90&quot;);">
                 <img src="https://akcdn.detik.net.id/visual/2025/02/12/kepala-bpom-taruna-ikrar_43.jpeg?w=250&amp;q=90" alt="BPOM Siap Kawal Makan Bergizi Gratis, Ini Tugas Utamanya" title="BPOM Siap Kawal Makan Bergizi Gratis, Ini Tugas Utamanya" class="" style="display: none;">            </span>
         </a>
      </div>
      <div class="media__text">
         <h2 class="media__subtitle">
           detikHealth         </h2>
         <h3 class="media__title">
            <a href="https://health.detik.com/berita-detikhealth/d-7777235/bpom-siap-kawal-makan-bergizi-gratis-ini-tugas-utamanya" dtr-evt="search result relevansi" dtr-sec="search result relevansi" dtr-act="artikel" onclick="_pt(this)" dtr-idx="3" dtr-id="7777235" dtr-ttl="BPOM Siap Kawal Makan Bergizi Gratis, Ini Tugas Utamanya" class="media__link">BPOM Siap Kawal Makan Bergizi Gratis, Ini Tugas Utamanya</a>
         </h3>
         <div class="media__desc">
            BPOM RI menerima kunjungan Kepala Kantor Komunikasi Kepresidenan terkait makan bergizi gratis (MBG). Tugas BPOM mengawal MBG dari produksi hingga distribusi.         </div>
         <div class="media__date">
            <span d-time="1739446241" title="Kamis, 13 Feb 2025 18:30 WIB">Kamis, 13 Feb 2025 18:30 WIB</span>         </div>
      </div>
   </div>
</article>
                        <!-- newsfeeed -->
<article class="list-content__item">
   <div class="media media--text-overlay media--image-radius block-link">
      <div class="media__image">
         <a dtr-evt="search result relevansi video" dtr-sec="search result relevansi video" dtr-act="artikel video" onclick="_pt(this)" dtr-idx="1" dtr-id="250213057" dtr-ttl="Video: Menyoal Wacana Alokasi Dana Riset dari Makan Gratis" href="https://20.detik.com/detikupdate/20250213-250213057/video-menyoal-wacana-alokasi-dana-riset-dari-makan-gratis" class="media__link" d-collected="250213057searchresultrelevansivideo">
         <span class="ratiobox ratiobox--16-9 lqd" style="background-image: url(&quot;https://cdnv.detik.com/videoservice/AdminTV/2025/02/13/de5b8507258e432283bbef0e6e9fe94b-20250213080110-0s.jpg?w=900&quot;);">
             <img src="https://cdnv.detik.com/videoservice/AdminTV/2025/02/13/de5b8507258e432283bbef0e6e9fe94b-20250213080110-0s.jpg?w=900" alt="Video: Menyoal Wacana Alokasi Dana Riset dari Makan Gratis" title="Video: Menyoal Wacana Alokasi Dana Riset dari Makan Gratis" class="" style="display: none;">         </span>
         </a>
         <div class="media__icon media__icon--top-right">
            <i class="icon icon--xs icon-play-bg"></i>
            00:57         </div>
      </div>
      <div class="media__text">
         <h2 class="media__subtitle">20Detik</h2>
         <h3 class="media__title">
            <a dtr-evt="search result relevansi video" dtr-sec="search result relevansi video" dtr-act="artikel video" onclick="_pt(this)" dtr-idx="1" dtr-id="250213057" dtr-ttl="Video: Menyoal Wacana Alokasi Dana Riset dari Makan Gratis" href="https://20.detik.com/detikupdate/20250213-250213057/video-menyoal-wacana-alokasi-dana-riset-dari-makan-gratis" class="media__link">Video: Menyoal Wacana Alokasi Dana Riset dari Makan Gratis</a>
         </h3>
         <div class="media__date">
            <span d-time="1739408520" title="Kamis, 13 Feb 2025 08:02 WIB">Kamis, 13 Feb 2025 08:02 WIB</span>         </div>
      </div>
   </div>
</article>
    
         
               
         <article class="list-content__item">
   <div class="media media--right media--image-radius block-link">
      <div class="media__image">
         <a href="https://finance.detik.com/berita-ekonomi-bisnis/d-7775988/pekan-depan-penerima-makan-bergizi-gratis-tembus-2-juta-orang" dtr-evt="search result relevansi" dtr-sec="search result relevansi" dtr-act="artikel" onclick="_pt(this)" dtr-idx="4" dtr-id="7775988" dtr-ttl="Pekan Depan, Penerima Makan Bergizi Gratis Tembus 2 Juta Orang" class="media__link" d-collected="7775988searchresultrelevansi">
            <span class="ratiobox ratiobox--4-3 lqd" style="background-image: url(&quot;https://akcdn.detik.net.id/visual/2025/01/10/siswa-antusias-menyantap-hidangan-makan-bergizi-gratis-di-smk-pgri-1-amlapura-karangasem-jumat-1012025-i-wayan-selamat-juniasa_43.jpeg?w=250&amp;q=90&quot;);">
                 <img src="https://akcdn.detik.net.id/visual/2025/01/10/siswa-antusias-menyantap-hidangan-makan-bergizi-gratis-di-smk-pgri-1-amlapura-karangasem-jumat-1012025-i-wayan-selamat-juniasa_43.jpeg?w=250&amp;q=90" alt="Pekan Depan, Penerima Makan Bergizi Gratis Tembus 2 Juta Orang" title="Pekan Depan, Penerima Makan Bergizi Gratis Tembus 2 Juta Orang" class="" style="display: none;">            </span>
         </a>
      </div>
      <div class="media__text">
         <h2 class="media__subtitle">
           detikFinance         </h2>
         <h3 class="media__title">
            <a href="https://finance.detik.com/berita-ekonomi-bisnis/d-7775988/pekan-depan-penerima-makan-bergizi-gratis-tembus-2-juta-orang" dtr-evt="search result relevansi" dtr-sec="search result relevansi" dtr-act="artikel" onclick="_pt(this)" dtr-idx="4" dtr-id="7775988" dtr-ttl="Pekan Depan, Penerima Makan Bergizi Gratis Tembus 2 Juta Orang" class="media__link">Pekan Depan, Penerima Makan Bergizi Gratis Tembus 2 Juta Orang</a>
         </h3>
         <div class="media__desc">
            Badan Gizi Nasional (BGN) targetkan penerima makan bergizi gratis (MBG) mencapai 2 juta orang pada 17 Februari, termasuk di Papua dan Papua Tengah.         </div>
         <div class="media__date">
            <span d-time="1739413807" title="Kamis, 13 Feb 2025 09:30 WIB">Kamis, 13 Feb 2025 09:30 WIB</span>         </div>
      </div>
   </div>
</article>
         
               
         <article class="list-content__item">
   <div class="media media--right media--image-radius block-link">
      <div class="media__image">
         <a href="https://news.detik.com/berita/d-7774517/jakarta-targetkan-557-dapur-umum-makan-bergizi-gratis-tahun-ini" dtr-evt="search result relevansi" dtr-sec="search result relevansi" dtr-act="artikel" onclick="_pt(this)" dtr-idx="5" dtr-id="7774517" dtr-ttl="Jakarta Targetkan 557 Dapur Umum Makan Bergizi Gratis Tahun Ini" class="media__link" d-collected="7774517searchresultrelevansi">
            <span class="ratiobox ratiobox--4-3 lqd" style="background-image: url(&quot;https://akcdn.detik.net.id/visual/2025/02/12/ketua-dprd-dki-jakarta-khoirudin-berbicara-soal-kegiatan-peninjauan-makan-bergizi-gratis-12-februari-2025-brigitta-belia-perma_43.jpeg?w=250&amp;q=90&quot;);">
                 <img src="https://akcdn.detik.net.id/visual/2025/02/12/ketua-dprd-dki-jakarta-khoirudin-berbicara-soal-kegiatan-peninjauan-makan-bergizi-gratis-12-februari-2025-brigitta-belia-perma_43.jpeg?w=250&amp;q=90" alt="Jakarta Targetkan 557 Dapur Umum Makan Bergizi Gratis Tahun Ini" title="Jakarta Targetkan 557 Dapur Umum Makan Bergizi Gratis Tahun Ini" class="" style="display: none;">            </span>
         </a>
      </div>
      <div class="media__text">
         <h2 class="media__subtitle">
           detikNews         </h2>
         <h3 class="media__title">
            <a href="https://news.detik.com/berita/d-7774517/jakarta-targetkan-557-dapur-umum-makan-bergizi-gratis-tahun-ini" dtr-evt="search result relevansi" dtr-sec="search result relevansi" dtr-act="artikel" onclick="_pt(this)" dtr-idx="5" dtr-id="7774517" dtr-ttl="Jakarta Targetkan 557 Dapur Umum Makan Bergizi Gratis Tahun Ini" class="media__link">Jakarta Targetkan 557 Dapur Umum Makan Bergizi Gratis Tahun Ini</a>
         </h3>
         <div class="media__desc">
            Pemprov Jakarta bersama DPRD DKI Jakarta meninjau SDN 01 Cipulir, Kebayoran Lama. Jakarta menargetkan punya 557 dapur umum untuk makan bergizi gratis.         </div>
         <div class="media__date">
            <span d-time="1739336091" title="Rabu, 12 Feb 2025 11:54 WIB">Rabu, 12 Feb 2025 11:54 WIB</span>         </div>
      </div>
   </div>
</article>
         
               
         <article class="list-content__item">
   <div class="media media--right media--image-radius block-link">
      <div class="media__image">
         <a href="https://www.detik.com/sumut/berita/d-7779751/prabowo-tegaskan-uang-untuk-makan-bergizi-gratis-ada" dtr-evt="search result relevansi" dtr-sec="search result relevansi" dtr-act="artikel" onclick="_pt(this)" dtr-idx="6" dtr-id="7779751" dtr-ttl="Prabowo Tegaskan Uang untuk Makan Bergizi Gratis Ada" class="media__link" d-collected="7779751searchresultrelevansi">
            <span class="ratiobox ratiobox--4-3 lqd" style="background-image: url(&quot;https://akcdn.detik.net.id/visual/2025/02/15/prabowo-subianto-dok-youtube-gerindratv-1_43.png?w=250&amp;q=90&quot;);">
                 <img src="https://akcdn.detik.net.id/visual/2025/02/15/prabowo-subianto-dok-youtube-gerindratv-1_43.png?w=250&amp;q=90" alt="Prabowo Tegaskan Uang untuk Makan Bergizi Gratis Ada" title="Prabowo Tegaskan Uang untuk Makan Bergizi Gratis Ada" class="" style="display: none;">            </span>
         </a>
      </div>
      <div class="media__text">
         <h2 class="media__subtitle">
           detikSumut         </h2>
         <h3 class="media__title">
            <a href="https://www.detik.com/sumut/berita/d-7779751/prabowo-tegaskan-uang-untuk-makan-bergizi-gratis-ada" dtr-evt="search result relevansi" dtr-sec="search result relevansi" dtr-act="artikel" onclick="_pt(this)" dtr-idx="6" dtr-id="7779751" dtr-ttl="Prabowo Tegaskan Uang untuk Makan Bergizi Gratis Ada" class="media__link">Prabowo Tegaskan Uang untuk Makan Bergizi Gratis Ada</a>
         </h3>
         <div class="media__desc">
            Presiden Prabowo Subianto menegaskan anggaran untuk program Makan Bergizi Gratis (MBG) aman, menanggapi kritik dan menjelaskan pencapaian Badan Gizi Nasional.         </div>
         <div class="media__date">
            <span d-time="1739611319" title="Sabtu, 15 Feb 2025 16:21 WIB">19 jam yang lalu</span>         </div>
      </div>
   </div>
</article>
         
                        <article class="list-content__item">
   <div class="media media--text-overlay media--image-radius block-link">
      <div class="media__image">
         <a dtr-evt="search result relevansi foto" dtr-sec="search result relevansi foto" dtr-act="artikel foto" onclick="_pt(this)" dtr-idx="1" dtr-id="7771790" dtr-ttl="Momen Prabowo Tinjau Makan Bergizi Gratis di Bogor" href="https://finance.detik.com/foto-bisnis/d-7771790/momen-prabowo-tinjau-makan-bergizi-gratis-di-bogor" class="media__link" d-collected="7771790searchresultrelevansifoto">
         <span class="ratiobox ratiobox--16-9 lqd" style="background-image: url(&quot;https://akcdn.detik.net.id/community/media/visual/2025/02/10/prabowo-tinjau-makan-bergizi-gratis-di-bogor-1_169.jpeg?w=200&amp;q=&quot;);">
          <img src="https://akcdn.detik.net.id/community/media/visual/2025/02/10/prabowo-tinjau-makan-bergizi-gratis-di-bogor-1_169.jpeg?w=200&amp;q=" alt="Momen Prabowo Tinjau Makan Bergizi Gratis di Bogor" title="Momen Prabowo Tinjau Makan Bergizi Gratis di Bogor" class="" style="display: none;">         </span>
         </a>
         <div class="media__icon media__icon--top-right">
            <i class="icon icon--xs icon-camera-bg"></i>
            4 Foto
         </div>
      </div>
      <div class="media__text">
                     <h2 class="media__subtitle">Foto Bisnis</h2>
                  <h3 class="media__title">
            <a dtr-evt="search result relevansi foto" dtr-sec="search result relevansi foto" dtr-act="artikel foto" onclick="_pt(this)" dtr-idx="1" dtr-id="7771790" dtr-ttl="Momen Prabowo Tinjau Makan Bergizi Gratis di Bogor" href="https://finance.detik.com/foto-bisnis/d-7771790/momen-prabowo-tinjau-makan-bergizi-gratis-di-bogor" class="media__link">Momen Prabowo Tinjau Makan Bergizi Gratis di Bogor</a>
         </h3>
         <div class="media__date">
            <span d-time="1739187024" title="Senin, 10 Feb 2025 18:30 WIB">Senin, 10 Feb 2025 18:30 WIB</span>         </div>
      </div>
   </div>
</article>
               
         <article class="list-content__item">
   <div class="media media--right media--image-radius block-link">
      <div class="media__image">
         <a href="https://news.detik.com/spotlight/d-7773759/pangkas-sana-sini-demi-makan-bergizi-gratis" dtr-evt="search result relevansi" dtr-sec="search result relevansi" dtr-act="artikel" onclick="_pt(this)" dtr-idx="7" dtr-id="7773759" dtr-ttl="Pangkas Sana-sini demi Makan Bergizi Gratis" class="media__link" d-collected="7773759searchresultrelevansi">
            <span class="ratiobox ratiobox--4-3 lqd" style="background-image: url(&quot;https://akcdn.detik.net.id/visual/2025/02/11/ilustrasi-anggaran-belanja-tambahan-makan-bergizi-gratis_43.jpeg?w=250&amp;q=90&quot;);">
                 <img src="https://akcdn.detik.net.id/visual/2025/02/11/ilustrasi-anggaran-belanja-tambahan-makan-bergizi-gratis_43.jpeg?w=250&amp;q=90" alt="Pangkas Sana-sini demi Makan Bergizi Gratis" title="Pangkas Sana-sini demi Makan Bergizi Gratis" class="" style="display: none;">            </span>
         </a>
      </div>
      <div class="media__text">
         <h2 class="media__subtitle">
           detikNews         </h2>
         <h3 class="media__title">
            <a href="https://news.detik.com/spotlight/d-7773759/pangkas-sana-sini-demi-makan-bergizi-gratis" dtr-evt="search result relevansi" dtr-sec="search result relevansi" dtr-act="artikel" onclick="_pt(this)" dtr-idx="7" dtr-id="7773759" dtr-ttl="Pangkas Sana-sini demi Makan Bergizi Gratis" class="media__link">Pangkas Sana-sini demi Makan Bergizi Gratis</a>
         </h3>
         <div class="media__desc">
            Kebutuhan anggaran untuk mengeksekusi program Makan Bergizi Gratis bergonta-ganti dan membengkak. Berujung pemangkasan anggaran kementerian dan lembaga.         </div>
         <div class="media__date">
            <span d-time="1739275625" title="Selasa, 11 Feb 2025 19:07 WIB">Selasa, 11 Feb 2025 19:07 WIB</span>         </div>
      </div>
   </div>
</article>
         
               
         <article class="list-content__item">
   <div class="media media--right media--image-radius block-link">
      <div class="media__image">
         <a href="https://finance.detik.com/berita-ekonomi-bisnis/d-7777941/prabowo-pede-makan-bergizi-dan-cek-kesehatan-gratis-bikin-orang-ri-hemat" dtr-evt="search result relevansi" dtr-sec="search result relevansi" dtr-act="artikel" onclick="_pt(this)" dtr-idx="8" dtr-id="7777941" dtr-ttl="Prabowo Pede Makan Bergizi dan Cek Kesehatan Gratis Bikin Orang RI Hemat" class="media__link" d-collected="7777941searchresultrelevansi">
            <span class="ratiobox ratiobox--4-3 lqd" style="background-image: url(&quot;https://akcdn.detik.net.id/visual/2025/02/13/presiden-prabowo-subianto-dok-istimewa_43.jpeg?w=250&amp;q=90&quot;);">
                 <img src="https://akcdn.detik.net.id/visual/2025/02/13/presiden-prabowo-subianto-dok-istimewa_43.jpeg?w=250&amp;q=90" alt="Prabowo Pede Makan Bergizi dan Cek Kesehatan Gratis Bikin Orang RI Hemat" title="Prabowo Pede Makan Bergizi dan Cek Kesehatan Gratis Bikin Orang RI Hemat" class="" style="display: none;">            </span>
         </a>
      </div>
      <div class="media__text">
         <h2 class="media__subtitle">
           detikFinance         </h2>
         <h3 class="media__title">
            <a href="https://finance.detik.com/berita-ekonomi-bisnis/d-7777941/prabowo-pede-makan-bergizi-dan-cek-kesehatan-gratis-bikin-orang-ri-hemat" dtr-evt="search result relevansi" dtr-sec="search result relevansi" dtr-act="artikel" onclick="_pt(this)" dtr-idx="8" dtr-id="7777941" dtr-ttl="Prabowo Pede Makan Bergizi dan Cek Kesehatan Gratis Bikin Orang RI Hemat" class="media__link">Prabowo Pede Makan Bergizi dan Cek Kesehatan Gratis Bikin Orang RI Hemat</a>
         </h3>
         <div class="media__desc">
            Presiden Prabowo Subianto pede program MBG dan Cek Kesehatan Gratis bisa bikin masyarakat hemat.         </div>
         <div class="media__date">
            <span d-time="1739502439" title="Jumat, 14 Feb 2025 10:07 WIB">Jumat, 14 Feb 2025 10:07 WIB</span>         </div>
      </div>
   </div>
</article>
         
               
         <article class="list-content__item">
   <div class="media media--right media--image-radius block-link">
      <div class="media__image">
         <a href="https://www.detik.com/jatim/berita/d-7772768/kapolres-gresik-tinjau-distribusi-makan-bergizi-gratis-di-sdn-71" dtr-evt="search result relevansi" dtr-sec="search result relevansi" dtr-act="artikel" onclick="_pt(this)" dtr-idx="9" dtr-id="7772768" dtr-ttl="Kapolres Gresik Tinjau Distribusi Makan Bergizi Gratis di SDN 71" class="media__link" d-collected="7772768searchresultrelevansi">
            <span class="ratiobox ratiobox--4-3 lqd" style="background-image: url(&quot;https://akcdn.detik.net.id/visual/2025/02/11/kapolres-dan-bupati-gresik-tinjau-distribusi-makan-bergizi-gratis-di-sdn-71_43.jpeg?w=250&amp;q=90&quot;);">
                 <img src="https://akcdn.detik.net.id/visual/2025/02/11/kapolres-dan-bupati-gresik-tinjau-distribusi-makan-bergizi-gratis-di-sdn-71_43.jpeg?w=250&amp;q=90" alt="Kapolres Gresik Tinjau Distribusi Makan Bergizi Gratis di SDN 71" title="Kapolres Gresik Tinjau Distribusi Makan Bergizi Gratis di SDN 71" class="" style="display: none;">            </span>
         </a>
      </div>
      <div class="media__text">
         <h2 class="media__subtitle">
           detikJatim         </h2>
         <h3 class="media__title">
            <a href="https://www.detik.com/jatim/berita/d-7772768/kapolres-gresik-tinjau-distribusi-makan-bergizi-gratis-di-sdn-71" dtr-evt="search result relevansi" dtr-sec="search result relevansi" dtr-act="artikel" onclick="_pt(this)" dtr-idx="9" dtr-id="7772768" dtr-ttl="Kapolres Gresik Tinjau Distribusi Makan Bergizi Gratis di SDN 71" class="media__link">Kapolres Gresik Tinjau Distribusi Makan Bergizi Gratis di SDN 71</a>
         </h3>
         <div class="media__desc">
            Bupati Gresik dan Kapolres bagikan 175 paket Makan Bergizi Gratis di SDN 71. Program ini mendukung kesehatan dan perkembangan anak-anak di Gresik.         </div>
         <div class="media__date">
            <span d-time="1739248538" title="Selasa, 11 Feb 2025 11:35 WIB">Selasa, 11 Feb 2025 11:35 WIB</span>         </div>
      </div>
   </div>
</article>
         
               
         <article class="list-content__item">
   <div class="media media--right media--image-radius block-link">
      <div class="media__image">
         <a href="https://www.detik.com/jateng/bisnis/d-7773724/menkeu-soal-makan-bergizi-gratis-prioritas-bukan-hanya-dalam-hal-budget" dtr-evt="search result relevansi" dtr-sec="search result relevansi" dtr-act="artikel" onclick="_pt(this)" dtr-idx="10" dtr-id="7773724" dtr-ttl="Menkeu soal Makan Bergizi Gratis: Prioritas Bukan Hanya dalam Hal Budget" class="media__link" d-collected="7773724searchresultrelevansi">
            <span class="ratiobox ratiobox--4-3 lqd" style="background-image: url(&quot;https://akcdn.detik.net.id/visual/2025/02/11/momen-sri-mulyani-hadiri-mandiri-investment-forum-4_43.jpeg?w=250&amp;q=90&quot;);">
                 <img src="https://akcdn.detik.net.id/visual/2025/02/11/momen-sri-mulyani-hadiri-mandiri-investment-forum-4_43.jpeg?w=250&amp;q=90" alt="Menkeu soal Makan Bergizi Gratis: Prioritas Bukan Hanya dalam Hal Budget" title="Menkeu soal Makan Bergizi Gratis: Prioritas Bukan Hanya dalam Hal Budget" class="" style="display: none;">            </span>
         </a>
      </div>
      <div class="media__text">
         <h2 class="media__subtitle">
           detikJateng         </h2>
         <h3 class="media__title">
            <a href="https://www.detik.com/jateng/bisnis/d-7773724/menkeu-soal-makan-bergizi-gratis-prioritas-bukan-hanya-dalam-hal-budget" dtr-evt="search result relevansi" dtr-sec="search result relevansi" dtr-act="artikel" onclick="_pt(this)" dtr-idx="10" dtr-id="7773724" dtr-ttl="Menkeu soal Makan Bergizi Gratis: Prioritas Bukan Hanya dalam Hal Budget" class="media__link">Menkeu soal Makan Bergizi Gratis: Prioritas Bukan Hanya dalam Hal Budget</a>
         </h3>
         <div class="media__desc">
            Menteri Keuangan Sri Mulyani menyatakan pelaksanaan program Makan Bergizi Gratis seperti menggelar pesta pernikahan setiap hari selama setahun.         </div>
         <div class="media__date">
            <span d-time="1739272748" title="Selasa, 11 Feb 2025 18:19 WIB">Selasa, 11 Feb 2025 18:19 WIB</span>         </div>
      </div>
   </div>
</article>
         
                     </div>

    '''

    @patch('requests.get')
    def test_search_valid_query(self, mock_get):
        mock_response = Mock()
        mock_response.text = self.html
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        scraper = DetikNewsScraper()
        result = scraper.search('makan bergizi gratis', 1)
        self.assertGreaterEqual(len(result), 1)

    @patch('requests.get')
    def test_search_invalid_query(self, mock_get):
        mock_response = Mock()
        mock_response.text = '<html></html>'
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        scraper = DetikNewsScraper()
        result = scraper.search('invalidquery', 1)
        self.assertEqual(len(result), 0)

    @patch('requests.get')
    def test_search_no_results(self, mock_get):
        mock_response = Mock()
        mock_response.text = '<html></html>'
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        scraper = DetikNewsScraper()
        result = scraper.search('test', 1)
        self.assertEqual(len(result), 0)

    @patch('requests.get')
    def test_detail(self, mock_get):
        mock_response = Mock()
        mock_response.text = '<html><div class="detail__body-text"><p>Paragraph 1</p><p>Paragraph 2</p></div></html>'
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        scraper = DetikNewsScraper()
        result = scraper.detail('https://news.detik.com/some-news')
        self.assertEqual(result, 'Paragraph 1Paragraph 2')

    @patch('requests.get')
    def test_get_article(self, mock_get):
        mock_response = Mock()
        mock_response.text = '<html><div class="detail__body-text"><p>Paragraph 1</p><p>Paragraph 2</p></div></html>'
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        scraper = DetikNewsScraper()
        result = scraper.get_article('https://news.detik.com/some-news')
        self.assertEqual(result, 'Paragraph 1Paragraph 2')

    @patch('requests.get')
    def test_result_count(self, mock_get):
        mock_response = Mock()
        mock_response.text = '<html><span class="fl text">About 100 results</span></html>'
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        scraper = DetikNewsScraper()
        result = scraper.result_count(mock_response)
        self.assertEqual(result, 100)

if __name__ == '__main__':
    unittest.main()