

document.getElementById("back_button").onclick = function(){
    location.href = "/information";
}


$(function(){
    window.setInterval(function(){
        loadNewDecimal()
    },2000)


    function loadNewDecimal(){
        $.ajax({
            url:"/update_decimal",
            type:"POST",
            dataType: "json",
            success: function(data){

                var values = data[1].split("\n")[1];

                values = values.split(",");

                rasp_id = sessionStorage.getItem("rasp_id");

                values[1] = values[1].replace("[","");
                values[1] = values[1].replace("]","");
                values[1] = values[1].replace("&#39;","");
                values[1] = values[1].replace("&#39;","").trim();
                fire_notifications = values[1].split(";");

                if(fire_notifications[rasp_id-1] == 0){
                    document.location.href = "./information";
                }

                for(let i=2;i<values.length;i++){

                    if((i-1) % 6 == 2){
                        if(values[i].trim() == rasp_id){
                            values[i+1] = values[i+1].replace("&#39;","");
                            fire_location = values[i+1].replace("&#39;","");
                            document.getElementById("fire_location").textContent = "Fire Location: " + fire_location;
                            break;
                        }
                    }
                }
                


                
                values[0] = values[0].replace("[","");
                values[0] = values[0].replace("]","");
                values[0] = values[0].replace("&#39;","");
                values[0] = values[0].replace("&#39;","").trim();
                values[values.length-1] = values[values.length-1].replace("]","");

                new_image_name = values[0].split(";")[rasp_id-1];
                var old_image_name = document.getElementById("image_div").childNodes[1].src.substring(46-10);

                var new_src = document.getElementById("image_div").childNodes[1].src.replace(old_image_name, new_image_name);

                document.getElementById("image_div").childNodes[1].src = new_src;
            }
        });
    }
});