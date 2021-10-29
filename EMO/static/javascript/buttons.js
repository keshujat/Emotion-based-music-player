
let play = document.getElementById("playBtn");
let music = document.querySelector('audio');
let prev = document.getElementById('prev');
let next = document.getElementById('next');
let stop = document.getElementById('stop');

let cnt = 0;

const songs = [
    {
        name:"0",
    },   
    {
        name:"1"
    },   
    {
        name:"2"
    },   
    {
        name:"3"
    },
    {
        name:"4"
    },
    {
        name:"5"
    },
    {
        name:"6"
    },
    {
        name:"7"
    },
    {
        name:"8"
    },
    {
        name:"9"
    },
    {
        name:"10"
    },
    {
        name:"11"
    },
    {
        name:"12"
    },    
    {
        name:"13"
    },
    {
        name:"14"
    },
    {
        name:"15"
    },
    {
        name:"16"
    },
    {
        name:"17"
    },
    {
        name:"18"
    },
    {
        name:"19"
    },
    {
        name:"20"
    },
    {
        name:"21"
    },
    {
        name:"22"
    },
]

const loadsong = (songs) => {
    //music.src = "{% static 'music/" + songs.name + ".mp3' %}";
    //console.log(songs.name);
    let play_song_list = songs.name;
    var src = music.getAttribute(play_song_list);
    music.setAttribute("src", src);
    //console.log();

}
//  loadsong(songs[0]);
song_index = 0;
const next_song = () => {
    song_index = (song_index + 1) % songs.length;
    loadsong(songs[song_index]);
    playmusic();
}
next.addEventListener('click',next_song);
const prev_song = () => {
    song_index = (song_index - 1 + songs.length) % songs.length;
    loadsong(songs[song_index]);
    playmusic();
}
prev.addEventListener('click',prev_song);
let isplaying = false;
const playmusic = () => {
    isplaying = true;
    music.play();
    play.classList.replace('fa-play','fa-pause');
}
const  pausemusic = () => {
    isplaying = false;
    music.pause();
    play.classList.replace('fa-pause','fa-play');
}
play.addEventListener('click',() => {
    if(isplaying == false){
        playmusic();
    }
    else{
        pausemusic();
    }
    
})
function click_on_particular(list_number){
    let play_the_song = 0;
    for(let i = 0;i<songs.length;i++){
        if(list_number == i){
            play_the_song = i;
        }
    }
    loadsong(songs[play_the_song]);
    playmusic();
}
stop.addEventListener('click',() => {
    pausemusic();
});