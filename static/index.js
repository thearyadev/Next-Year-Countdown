$("#days").text("0")
$("#hours").text("0")
$("#minutes").text("0")
$("#seconds").text("0")

function pick_color() {
    const colors = [
        "#32a8a8",
        "#a89832",
        "#7a15ba",
        "#55b81d",
    ]
    const random = Math.floor(Math.random() * colors.length);
    return colors[random]

}


$("body").css("background-color", pick_color());


setInterval(function () {
    $.ajax({
        url: "/api/time-till",
        success: function (data) {
            $("#headline").text("COUNTDOWN TO " + data.year)
            $("#days").text(data.days)
            $("#hours").text(data.hours)
            $("#minutes").text(data.minutes)
            $("#seconds").text(data.seconds)
        }
    })

}, 1000)