

document.getElementById("stop_sensing_button").onclick = function(){
    location.href = "/stop_sensing";
}


document.getElementById("rasp_1_fire_button").onclick = function(){
    sessionStorage.setItem("rasp_id", 1);
    location.href = "/fire_image"
  };

  document.getElementById("rasp_2_fire_button").onclick = function(){
    sessionStorage.setItem("rasp_id", 2);
    location.href = "/fire_image"
  };
  
  document.getElementById("rasp_3_fire_button").onclick = function(){
    sessionStorage.setItem("rasp_id", 3);
    location.href = "/fire_image"
  };

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

                  values[0] = values[0].replace("[","");
                  values[values.length-1] = values[values.length-1].replace("]","");

                  fire_images = values[0].split(";");

                  values[1] = values[1].replace("[","");
                  values[1] = values[1].replace("]","");
                  values[1] = values[1].replace("&#39;","");
                  values[1] = values[1].replace("&#39;","").trim();
                  fire_notifications = values[1].split(";");

                  for(i=1;i<fire_notifications.length+1;i++){
                    button_id = "rasp_" + i +"_fire_button"
                    if(fire_notifications[i-1] == 0){
                      document.getElementById(button_id).disabled = true;
                      document.getElementById(button_id).className = "btn btn-secondary";
                    }
                    else{
                      document.getElementById(button_id).disabled = false;
                      document.getElementById(button_id).className = "btn btn-danger";
                    }
                  }
                  c=2;
                  for(let i=2;i<values.length;i++){
                      id_str = "val"+(c-1);

                      if(typeof(values[i]) === 'string'){
                          values[i] = values[i].replace("&#39;","");
                          values[i] = values[i].replace("&#39;","");
                      }
                      if(values[i] == " "){
                        continue;
                      }
                      document.getElementById(id_str).textContent = values[i].trim();
                      c+=1;
                  }
              }
          });
      }
  });