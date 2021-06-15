const form=document.querySelector('form');



const usernameField = document.querySelector('#id_username');
const passwordField = document.querySelector('#id_password');

usernameField.setAttribute('class', 'form-control');
passwordField.setAttribute('class', 'form-control');
//======================================================================

const usernamefield=form.username;
const error_message = error_username.innerHTML;
const result={
    username:false,
    password:false
    
};

form.addEventListener("submit",(e)=>
{
//    alert(result.username+" "+result.email+" " + result.password+ result.contact_no);
    if(result.username  && result.password )
        return true
    e.preventDefault();
    return false

});

const inputs = document.querySelectorAll("input");
const font_tag=document.querySelector(".fa");
const patterns={
username: /^[a-zA-Z\d@_]{5,20}$/,
password: /^[a-zA-Z\d@]{6,20}$/,
};
function validate(field,pattern)
{
    let valid_field   =  document.querySelector("#help_"+field.attributes.name.value);
    let inValid_field =  document.querySelector("#error_"+field.attributes.name.value);
    // console.log(valid_field);
    // console.log(inValid_field);

    if(pattern.test(field.value))
    {
        field.classList.replace('fail','success');
        result[field.attributes.name.value]=true;
    }
    else{
        if(field.classList.contains('success'))
        {
            field.classList.replace('success','fail');
        }
        
        field.classList.add('fail');
        result[field.attributes.name.value]=false;
        

    }
}

function calc(field,pattern)
{
    let valid_field   =  document.querySelector("#help_"+field.attributes.name.value);
    let inValid_field =  document.querySelector("#error_"+field.attributes.name.value);
    if(pattern.test(field.value))
    {
        valid_field.classList.add('show');
        if(valid_field.classList.contains("hide"))
        {
            valid_field.classList.replace("hide",'show')

        }
        inValid_field.classList.replace('show','hide');
        

    }
    else{
        // valid_field.classList.replace("show",'hide');
        if(valid_field.classList.contains("show"))
        {
            valid_field.classList.replace("show",'hide');
        }
        inValid_field.classList.replace('hide','show');


        valid_field.classList.add('hide');
        // inValid_field.classList.add('show');
    }
}

inputs.forEach((input)=>
{
    input.addEventListener('keyup',(event)=>
    {
        let pattern=patterns[event.target.attributes.name.value];
        console.log(pattern);
        let field=event.target;
        if(field.attributes.name.value=='username')
        {
            // const error_username=document.querySelector('#error_username');
            error_username.innerHTML=error_message;
            
        }
        validate(field,pattern);
    input.addEventListener("blur",(e)=>
    {
        calc(field,pattern);
    });
        

    });

})



//---------------------------------password visiblity---------------------------------------------------
let visiblity=false;
const eye_ico=document.querySelector("#f_eye");
const id_password=document.querySelector("#id_password");
// console.log(id_password.innerHTML=="")
eye_ico.addEventListener("click",(e)=>
{
    if(!visiblity && id_password.value!="" )
    {
        id_password.attributes.type.value="text";
        eye_ico.classList.add("text-danger");
        if(eye_ico.classList.contains("text-dark"))
        {
            eye_ico.classList.replace("text-dark","text-danger");
        }
        visiblity=true;
    }
    else{
        id_password.attributes.type.value="password";
        eye_ico.classList.replace("text-danger","text-dark");
        visiblity=false;

    }


})
