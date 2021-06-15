const selectCity=document.querySelector("#select-city");
console.log(selectCity);

const _getAllCity=async ()=>
{
    const response=await fetch("/cities/");
    return response.json()
}
_getAllCity().then((cities)=>
{    cities.forEach((city) => {
        let a=document.createElement('a');
        console.log(city);
        a.setAttribute("id","city"+city.pk);
        a.innerHTML=city.fields.city;
        a.classList.add("dropdown-item");
        a.href="#";
        console.log(selectCity.appendChild(a));
        console.log(a);
         
     });
     
     
}).catch((error)=>
{
    console.error(error);
})