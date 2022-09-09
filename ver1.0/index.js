btn.onclick = function() {
   const manual = document.getElementById('man');
   const mode = document.getElementById('mode');
   const xhr = new XMLHttpRequest();
   xhr.open('GET', 'http://127.0.0.1:8000/mode'+'?flag='+mode.value);
   xhr.send();
   xhr.onreadystatechange = function(){
    if(xhr.readyState === 4){
        if(xhr.status >= 200 && xhr.status < 300){
            manual.style.display = "inline-block";
        }
        else{
            alert("CONNECTION ERROR! STATUS:"+xhr.status);
        }
    }
   }
}