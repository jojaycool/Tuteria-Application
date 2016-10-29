$(document).ready(function(){

/* Search */

    $(".nav_search > a").click(function() {
        $('.search_pop').toggle();
        $(this).toggleClass('close');
    });

/* Promo */

    $('#slider').anythingSlider({
    	autoPlay        : true,
        buildStartStop  : false,
        delay           : 6000,
        startPanel      : 1,
        hashTags        : false,
    });

/* Clear Comment Box */

	$('#id_comment').focus(function() {
		var full = 'Post a comment...';
		if($(this).val() == full){
        	$(this).val('');
    	};
    });

/* Nav */

    $(function () {
        $('#header ul > li').hover(
            function () {
                $(this).find('ul').show();
                $(this).find('a').css({"z-index":"10"});
            },
            function () {
                $(this).find('ul').hide();
                $(this).find('a').css({"z-index":"0"});
            }
        );
    });

/* Validate */

    $('#frmContact').validate();
    $('#frmCompetition').validate();
    $('#frmPoll').validate();

/* General Chops */

    $(function () {
        $('.brand_item:nth-child(3n)').css({"border-right":"0"});
        $('#interact .third:nth-child(3n)').css({"margin":"0"});
    });

});