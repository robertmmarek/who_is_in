let parseHashtags = function(text){
    let re = /#([A-Za-z0-9]+)/g;
    let result = [];
    while((res = re.exec(text)) !== null){
        result.push(res[1]);
    }
    return result;
}

let date = document.getElementById('happeningDate');

$('input[name="date_noniso"]').daterangepicker({
    singleDatePicker: true,
    showDropdowns: true,
    timePicker: true,
    startDate: moment().startOf('hour')
}, function(start, end, label){
    date.value = start.format('YYYY-MM-DD HH:MM:SS');
    console.log(date.value);
});

window.addEventListener('load', function(){
    let form = document.getElementById('createHappeningForm');
    let description = document.getElementById('happeningDescription');
    let hashtagsInput = document.getElementById('hashtags');

    form.addEventListener('submit', function(event){
        let hashtags = parseHashtags(description.value);
        hashtags.forEach(element => {
            let hashtagInput = document.createElement("input");
            hashtagInput.classList.add("form-control");
            hashtagInput.name = "hashtag";
            hashtagInput.value = element;
            hashtagsInput.appendChild(hashtagInput);
        });
    }, false);

}, false);