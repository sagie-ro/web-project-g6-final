const origin= document.getElementById('origin');
const form=document.getElementById('form');
const errorElement= document.getElementById('error');

form.addEventListener('submit', (e)=> {
    let massages=[];
    if(origin.value==null || origin.value===''){
        massages.push('origin is required')
    }

    if(massages.length>0){
        e.preventDefault()
    }
})