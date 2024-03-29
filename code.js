var songrun = false;
var count = 1;
var mod = 1;
var path = ["songs/ban ja rani.mp3",
    "songs/Banduk meri laila.mp3",
    "songs/barish.mp3",
    "songs/haareya.mp3",
    "songs/ik vari aa.mp3",
    "songs/main tera.mp3",
    "songs/mercy.mp3",
    "songs/musafir.mp3",
    "songs/o sathi.mp3",
    "songs/phir bhi.mp3"
];

var sname = ["Ban Ja tu meri Rani",
    "Banduk Meri Laila",
    "Barish",
    "Haareya",
    "Ik vari aa",
    "main tera boyfriend",
    "mercy",
    "musafir",
    "o sathi",
    "Phir Bhi"
];

var sd = ["Artist: Guru Randhawa<br>Movie: Tumhari Sulu<br>Released: 2017",
    "Artists: Ash King, Jigar Saraiya<br>Featured artists: Sidharth Malhotra, Raftaar<br>Movie: A Gentleman<br>Released: 2017",
    "Artists: Ash King, Shashaa Tirupati<br>Movie: Half Girlfriend<br>Released: 2017<br>Awards: Zee Cine Award for Song of the Year",
    "Artist: Arijit Singh<br>Movie: Meri Pyaari Bindu<br>Released: 2017<br>Nominations: Mirchi Music Awards for Best Song Producer - Programming & Arranging",
    "Artist: Arijit Singh<br>Movie: Raabta<br>Released: 2017",
    "Artists: Arijit Singh, Neha Kakkar, Meet Bros<br>Movie: Raabta<br>Released: 2017<br>Composer(s): : Sohrabbudin (Original); Sourav Roy (Revamped).<br>Genre: Dance music",
    "Artist: Badshah<br>Released: 2017<br>Nominations: Mirchi Music Awards for Best Song Engineer - Recording and Mixing",
    "Artist: KK<br>Movie: Shab<br>Released: 2017",
    "Artist: Arijit Singh<br>Movie: Shab<br>Released: 2017",
    "Artists: Arijit Singh, Shashaa Tirupati<br>Movie: Half Girlfriend<br>Released: 2017<br>Written: 2001 (lyrics)<br>Lyricist(s): Manoj Muntashir<br>Composer(s): Mithoon"
];

var bool = [];
for (var i = 0; i < sd.length; i++)
    bool[i] = false;

var icon = ["images/1.jpg",
    "images/2.jpg",
    "images/3.jpg",
    "images/4.jpg",
    "images/5.jpg",
    "images/6.jpg",
    "images/7.jpg",
    "images/8.jpg",
    "images/9.jpg",
    "images/10.jpg"
];

var mood = [
    ["1", "2", "3"],
    ["4", "5"],
    ["6", "7", "8"],
    ["9", "10"]
];
var mmm = ["1.png", "1.png", "1.png", "2.png", "2.png", "3.png", "3.png", "3.png", "4.png", "4.png"];

var songs = new Array(icon.length);
for (var i = 0; i < icon.length; i++) {
    songs[i] = new Array(4);
    songs[i][0] = path[i];
    songs[i][1] = sd[i];
    songs[i][2] = icon[i];
    songs[i][3] = mmm[i];
    console.log(songs[i][0]);
    console.log(songs[i][1]);
    console.log(songs[i][2]);
    var ins = document.createElement("div");
    ins.id = 'b' + i;
    ins.className = 'song';
    ins.innerHTML = '<div id="pic" style="background-image: url(\'' + songs[i][2] + '\');">  <input type="button" id="' + "a" + i + '" class="play" > <input type="button" id="' + "c" + i + '" class="add">  </div><div id="data"><br><br>' + songs[i][1] + '</div>';
    document.body.appendChild(ins);

    document.getElementById('a' + i).addEventListener('click', function() {
        play(this);
    });

    document.getElementById('c' + i).addEventListener('click', function() {
        addq(this);
    });
}
