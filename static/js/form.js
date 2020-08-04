console.log('it works')
function addForm() {
    var $templateForm = $('#skill-_-form');
    console.log('i am here now')

    if (!$templateForm) {
        console.log('[ERROR] Cannot find template');
        return;
    }

    // Get Last index
    var $lastForm = $('.skill-subform').last();

    var newIndex = 0;

    if ($lastForm.length > 0) {
        newIndex = parseInt($lastForm.data('index')) + 1;
    }

    // Maximum of 20 subforms
    if (newIndex > 20) {
        console.log('[WARNING] Reached maximum number of elements');
        return;
    }

    // Add elements
    var $newForm = $templateForm.clone();

    $newForm.attr('id', $newForm.attr('id').replace('_', newIndex));
    $newForm.data('index', newIndex);

    $newForm.find('input').each(function(idx) {
        var $item = $(this);

        $item.attr('id', $item.attr('id').replace('_', newIndex));
        $item.attr('name', $item.attr('name').replace('_', newIndex));
    });

    // Append
    $('#skill-container').append($newForm);
    $newForm.addClass('skill-subform');
    $newForm.removeClass('is_hidden');

}

$(document).ready(function() {
    $('#addSkill').click(addForm);
});


// EXPERIENCE
function addExperience() {
    var $templateForm = $('#experience-_-Form');
    console.log('i am here now')

    if (!$templateForm) {
        console.log('[ERROR] Cannot find template');
        return;
    }

    // Get Last index
    var $lastForm = $('.experience-subform').last();

    var newIndex = 0;

    if ($lastForm.length > 0) {
        newIndex = parseInt($lastForm.data('index')) + 1;
    }

    // Maximum of 20 subforms
    if (newIndex > 20) {
        console.log('[WARNING] Reached maximum number of elements');
        return;
    }

    // Add elements
    var $newForm = $templateForm.clone();

    $newForm.attr('id', $newForm.attr('id').replace('_', newIndex));
    $newForm.data('index', newIndex);

    $newForm.find('input').each(function(idx) {
        var $item = $(this);

        $item.attr('id', $item.attr('id').replace('_', newIndex));
        $item.attr('name', $item.attr('name').replace('_', newIndex));
    });

    if ($newForm.find('textarea')!= '') {

    $newForm.find('textarea').each(function(idx) {
        var $item = $(this);

        $item.attr('id', $item.attr('id').replace('_', newIndex));
        $item.attr('name', $item.attr('name').replace('_', newIndex));
    });

    }


    // Append
    $('#experience-container').append($newForm);
    $newForm.addClass('experience-subform');
    $newForm.removeClass('is_hidden');

}


$(document).ready(function() {
    $('#addExperience').click(addExperience);
});




// EXPERTISE
function addExpertise() {
    var $templateForm = $('#expertise-_-form');

    if (!$templateForm) {
        console.log('[ERROR] Cannot find template');
        return;
    }

    // Get Last index
    var $lastForm = $('.expertise-subform').last();

    var newIndex = 0;

    if ($lastForm.length > 0) {
        newIndex = parseInt($lastForm.data('index')) + 1;
    }

    // Maximum of 20 subforms
    if (newIndex > 20) {
        console.log('[WARNING] Reached maximum number of elements');
        return;
    }

    // Add elements
    var $newForm = $templateForm.clone();

    $newForm.attr('id', $newForm.attr('id').replace('_', newIndex));
    $newForm.data('index', newIndex);

    $newForm.find('input').each(function(idx) {
        var $item = $(this);

        $item.attr('id', $item.attr('id').replace('_', newIndex));
        $item.attr('name', $item.attr('name').replace('_', newIndex));
    });

    if ($newForm.find('textarea')!= '') {

    $newForm.find('textarea').each(function(idx) {
        var $item = $(this);

        $item.attr('id', $item.attr('id').replace('_', newIndex));
        $item.attr('name', $item.attr('name').replace('_', newIndex));
    });

    }


    // Append
    $('#expertise-container').append($newForm);
    $newForm.addClass('expertise-subform');
    $newForm.removeClass('is_hidden');

}


$(document).ready(function() {
    console.log('here')
    $('#addExpertise').click(addExpertise);
});





// PROJECTS
function addProjects() {
    var $templateForm = $('#projects-_-form');

    if (!$templateForm) {
        console.log('[ERROR] Cannot find template');
        return;
    }

    // Get Last index
    var $lastForm = $('.projects-subform').last();

    var newIndex = 0;

    if ($lastForm.length > 0) {
        newIndex = parseInt($lastForm.data('index')) + 1;
    }

    // Maximum of 20 subforms
    if (newIndex > 20) {
        console.log('[WARNING] Reached maximum number of elements');
        return;
    }

    // Add elements
    var $newForm = $templateForm.clone();

    $newForm.attr('id', $newForm.attr('id').replace('_', newIndex));
    $newForm.data('index', newIndex);

    $newForm.find('input').each(function(idx) {
        var $item = $(this);

        $item.attr('id', $item.attr('id').replace('_', newIndex));
        $item.attr('name', $item.attr('name').replace('_', newIndex));
    });

    if ($newForm.find('textarea')!= '') {

    $newForm.find('textarea').each(function(idx) {
        var $item = $(this);

        $item.attr('id', $item.attr('id').replace('_', newIndex));
        $item.attr('name', $item.attr('name').replace('_', newIndex));
    });

    }


    // Append
    $('#projects-container').append($newForm);
    $newForm.addClass('projects-subform');
    $newForm.removeClass('is_hidden');

}


$(document).ready(function() {
    $('#addProjects').click(addProjects);
});
