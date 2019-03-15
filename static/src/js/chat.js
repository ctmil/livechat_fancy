function openChat () {
        if (document.getElementsByClassName("o_livechat_button").length >= 1) {
                document.getElementsByClassName("o_livechat_button")[0].click();
        }
}

function load () {
        interval = setInterval(function (){
                var el = document.getElementById("button_chat");
                el.addEventListener("click", openChat, false);

                if (document.getElementsByClassName("o_livechat_button").length >= 1) {
                        document.getElementById("online").style.display = "block";
                        document.getElementById("offline").style.display = "none";
                        document.getElementById("button_chat").style.display = "block";
                        clearInterval(interval);
                } else {
                        document.getElementById("online").style.display = "none";
                        document.getElementById("offline").style.display = "block";
                        document.getElementById("button_chat").style.display = "none";
                }
        }, 1000);
}

document.addEventListener("DOMContentLoaded", load, false);
