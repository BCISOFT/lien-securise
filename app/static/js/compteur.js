window.addEventListener('load', (event) =>{
    if (document.getElementById("compteur") !== null) {
        let zoneMessage=document.getElementById("ots_content");
        let NbreMax = 1024;
        document.getElementById("compteur").innerHTML = NbreMax;
        document.getElementById("fin_txt_compteur").innerHTML= ' caractères';

        zoneMessage.onfocus=function(){
            posCur=zoneMessage.value.length;
            if(posCur>0){
                zoneMessage.setSelectionRange(0,0);
            }

        };

        zoneMessage.onkeyup=function(){
            let carRestants = NbreMax - this.value.length;
            if(carRestants > 1) {
                document.getElementById("compteur").innerHTML = carRestants;
                document.getElementById("fin_txt_compteur").innerHTML = ' caractères';
            }else{
                document.getElementById("compteur").innerHTML = carRestants;
                document.getElementById("fin_txt_compteur").innerHTML = ' caractère';
            }
        }
    }
});