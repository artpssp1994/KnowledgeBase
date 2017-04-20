/**
 * Created by vacharapat on 7/6/2015 AD.
 */

$(document).ready(function(){
    $.get('/profile/general_profile_panel/', {}, function(data){
        $('#general_profile_panel').html(data);
    });
});