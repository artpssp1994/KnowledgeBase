{% extends 'user_menu.html' %}

{% block detail_block %}
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Tag-it! Example</title>

<!-- These few CSS files are just to make this example page look nice. You can ignore them. -->
<link rel="stylesheet" type="text/css" href="http://yui.yahooapis.com/2.9.0/build/reset-fonts/reset-fonts.css">
<link rel="stylesheet" type="text/css" href="http://yui.yahooapis.com/2.9.0/build/base/base-min.css">
<link href="http://fonts.googleapis.com/css?family=Brawler" rel="stylesheet" type="text/css">
<link href="_static/master.css" rel="stylesheet" type="text/css">
<link href="_static/subpage.css" rel="stylesheet" type="text/css">
<link href="_static/examples.css" rel="stylesheet" type="text/css">
<!-- /ignore -->


<!-- INSTRUCTIONS -->

<!-- 2 CSS files are required: -->
<!--   * Tag-it's base CSS (jquery.tagit.css). -->
<!--   * Any theme CSS (either a jQuery UI theme such as "flick", or one that's bundled with Tag-it, e.g. tagit.ui-zendesk.css as in this example.) -->
                                                                             <!-- The base CSS and tagit.ui-zendesk.css theme are scoped to the Tag-it widget, so they shouldn't affect anything else in your site, unlike with jQuery UI themes. -->
                                                                                                                                                                              <link href="css/jquery.tagit.css" rel="stylesheet" type="text/css">
                                                                                                                                                                                                                                      <link href="css/tagit.ui-zendesk.css" rel="stylesheet" type="text/css">
                                                                                                                                                                                                                                                                                                  <!-- If you want the jQuery UI "flick" theme, you can use this instead, but it's not scoped to just Tag-it like tagit.ui-zendesk is: -->
                                                                                                                                                                                                                                                                                                                                                                                <!--   <link rel="stylesheet" type="text/css" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1/themes/flick/jquery-ui.css"> -->

<!-- jQuery and jQuery UI are required dependencies. -->
<!-- Although we use jQuery 1.4 here, it's tested with the latest too (1.8.3 as of writing this.) -->
                                        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js" type="text/javascript" charset="utf-8"></script>
                                                                                                                                                                <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.9.2/jquery-ui.min.js" type="text/javascript" charset="utf-8"></script>

                                                                                                                                                                                                                                                                                             <!-- The real deal -->
<script src="js/tag-it.js" type="text/javascript" charset="utf-8"></script>

                                                                    <style>
                                                                    ul.tagit {
    padding: 1px 5px;
overflow: auto;
margin-left: inherit; /* usually we don't want the regular ul margins. */
margin-right: inherit;
}
ul.tagit li {
    display: block;
float: left;
margin: 2px 5px 2px 0;
}
ul.tagit li.tagit-choice {
    position: relative;
line-height: inherit;
}
input.tagit-hidden-field {
    display: none;
}
ul.tagit li.tagit-choice-read-only {
    padding: .2em .5em .2em .5em;
}

ul.tagit li.tagit-choice-editable {
    padding: .2em 18px .2em .5em;
}

ul.tagit li.tagit-new {
    padding: .25em 4px .25em 0;
}

ul.tagit li.tagit-choice a.tagit-label {
    cursor: pointer;
text-decoration: none;
}
ul.tagit li.tagit-choice .tagit-close {
    cursor: pointer;
position: absolute;
right: .1em;
top: 50%;
margin-top: -8px;
line-height: 17px;
}

/* used for some custom themes that don't need image icons */
ul.tagit li.tagit-choice .tagit-close .text-icon {
display: none;
}

ul.tagit li.tagit-choice input {
    display: block;
float: left;
margin: 2px 5px 2px 0;
}
ul.tagit input[type="text"] {
    -moz-box-sizing:    border-box;
-webkit-box-sizing: border-box;
box-sizing:         border-box;

-moz-box-shadow: none;
-webkit-box-shadow: none;
box-shadow: none;

border: none;
margin: 0;
padding: 0;
width: inherit;
background-color: inherit;
outline: none;
}

/* Optional scoped theme for tag-it which mimics the zendesk widget. */


ul.tagit {
border-style: solid;
border-width: 1px;
border-color: #C6C6C6;
background: inherit;
}
ul.tagit li.tagit-choice {
    -moz-border-radius: 6px;
border-radius: 6px;
-webkit-border-radius: 6px;
border: 1px solid #CAD8F3;

background: none;
background-color: #DEE7F8;

font-weight: normal;
}
ul.tagit li.tagit-choice .tagit-label:not(a) {
    color: #555;
}
ul.tagit li.tagit-choice a.tagit-close {
    text-decoration: none;
}
ul.tagit li.tagit-choice .tagit-close {
    right: .4em;
}
ul.tagit li.tagit-choice .ui-icon {
    display: none;
}
ul.tagit li.tagit-choice .tagit-close .text-icon {
    display: inline;
font-family: arial, sans-serif;
font-size: 16px;
line-height: 16px;
color: #777;
}
ul.tagit li.tagit-choice:hover, ul.tagit li.tagit-choice.remove {
    background-color: #bbcef1;
        border-color: #6d95e0;
}
ul.tagit li.tagit-choice a.tagLabel:hover,
                                    ul.tagit li.tagit-choice a.tagit-close .text-icon:hover {
    color: #222;
}
ul.tagit input[type="text"] {
    color: #333333;
        background: none;
}
.ui-widget {
    font-size: 1.1em;
}

/* Forked from a jQuery UI theme, so that we don't require the jQuery UI CSS as a dependency. */
                                                    .tagit-autocomplete.ui-autocomplete { position: absolute; cursor: default; }
* html .tagit-autocomplete.ui-autocomplete { width:1px; } /* without this, the menu expands to 100% in IE6 */
.tagit-autocomplete.ui-menu {
    list-style:none;
padding: 2px;
margin: 0;
display:block;
float: left;
}
.tagit-autocomplete.ui-menu .ui-menu {
    margin-top: -3px;
}
.tagit-autocomplete.ui-menu .ui-menu-item {
    margin:0;
padding: 0;
zoom: 1;
float: left;
clear: left;
width: 100%;
}
.tagit-autocomplete.ui-menu .ui-menu-item a {
    text-decoration:none;
display:block;
padding:.2em .4em;
line-height:1.5;
zoom:1;
}
.tagit-autocomplete .ui-menu .ui-menu-item a.ui-state-hover,
.tagit-autocomplete .ui-menu .ui-menu-item a.ui-state-active {
    font-weight: normal;
margin: -1px;
}
.tagit-autocomplete.ui-widget-content { border: 1px solid #aaaaaa; background: #ffffff 50% 50% repeat-x; color: #222222; }
                                                        .tagit-autocomplete.ui-corner-all, .tagit-autocomplete .ui-corner-all { -moz-border-radius: 4px; -webkit-border-radius: 4px; -khtml-border-radius: 4px; border-radius: 4px; }
.tagit-autocomplete .ui-state-hover, .tagit-autocomplete .ui-state-focus { border: 1px solid #999999; background: #dadada; font-weight: normal; color: #212121; }
                                                                                           .tagit-autocomplete .ui-state-active  { border: 1px solid #aaaaaa; }

                                                                                                                                                   .tagit-autocomplete .ui-widget-content { border: 1px solid #aaaaaa; }
                                                                                                                                                                                                            .tagit .ui-helper-hidden-accessible { position: absolute !important; clip: rect(1px,1px,1px,1px); }



</style>

  <script>
$(function(){
    var sampleTags = ['c++', 'java', 'php', 'coldfusion', 'javascript', 'asp', 'ruby', 'python', 'c', 'scala', 'groovy', 'haskell', 'perl', 'erlang', 'apl', 'cobol', 'go', 'lua'];

//-------------------------------
  // Minimal
  //-------------------------------
$('#myTags').tagit();

//-------------------------------
  // Single field
            //-------------------------------
$('#singleFieldTags').tagit({
                                availableTags: sampleTags,
                            // This will make Tag-it submit a single form value, as a comma-delimited field.
    singleField: true,
                 singleFieldNode: $('#mySingleField')
});

// singleFieldTags2 is an INPUT element, rather than a UL as in the other
                                                                    // examples, so it automatically defaults to singleField.
$('#singleFieldTags2').tagit({
    availableTags: sampleTags
});

//-------------------------------
  // Preloading data in markup
                        //-------------------------------
$('#myULTags').tagit({
                         availableTags: sampleTags, // this param is of course optional. it's for autocomplete.
                                                                                           // configure the name of the input field (will be submitted with form), default: item[tags]
itemName: 'item',
          fieldName: 'tags'
});

//-------------------------------
  // Tag events
         //-------------------------------
var eventTags = $('#eventTags');

var addEvent = function(text) {
$('#events_container').append(text + '<br>');
};

eventTags.tagit({
    availableTags: sampleTags,
    beforeTagAdded: function(evt, ui) {
if (!ui.duringInitialization) {
    addEvent('beforeTagAdded: ' + eventTags.tagit('tagLabel', ui.tag));
}
},
afterTagAdded: function(evt, ui) {
if (!ui.duringInitialization) {
    addEvent('afterTagAdded: ' + eventTags.tagit('tagLabel', ui.tag));
}
},
beforeTagRemoved: function(evt, ui) {
    addEvent('beforeTagRemoved: ' + eventTags.tagit('tagLabel', ui.tag));
},
afterTagRemoved: function(evt, ui) {
    addEvent('afterTagRemoved: ' + eventTags.tagit('tagLabel', ui.tag));
},
onTagClicked: function(evt, ui) {
    addEvent('onTagClicked: ' + eventTags.tagit('tagLabel', ui.tag));
},
onTagExists: function(evt, ui) {
    addEvent('onTagExists: ' + eventTags.tagit('tagLabel', ui.existingTag));
}
});

//-------------------------------
  // Read-only
          //-------------------------------
$('#readOnlyTags').tagit({
    readOnly: true
});

//-------------------------------
  // Tag-it methods
            //-------------------------------
$('#methodTags').tagit({
    availableTags: sampleTags
});

//-------------------------------
  // Allow spaces without quotes.
                          //-------------------------------
$('#allowSpacesTags').tagit({
    availableTags: sampleTags,
    allowSpaces: true
});

//-------------------------------
  // Remove confirmation
            //-------------------------------
$('#removeConfirmationTags').tagit({
    availableTags: sampleTags,
    removeConfirmation: true
});

});
/*
* jQuery UI Tag-it!
*
* @version v2.0 (06/2011)
             *
             * Copyright 2011, Levy Carneiro Jr.
                                             * Released under the MIT license.
                                                                      * http://aehlke.github.com/tag-it/LICENSE
                                                                                                     *
                                                                                                     * Homepage:
*   http://aehlke.github.com/tag-it/
                                 *
                                 * Authors:
*   Levy Carneiro Jr.
                  *   Martin Rehfeld
                             *   Tobias Schmidt
                                        *   Skylar Challand
                                                   *   Alex Ehlke
                                                            *
                                                            * Maintainer:
*   Alex Ehlke - Twitter: @aehlke
*
* Dependencies:
*   jQuery v1.4+
*   jQuery UI v1.8+
*/
(function($) {

$.widget('ui.tagit', {
    options: {
                 allowDuplicates   : false,
                 caseSensitive     : true,
                 fieldName         : 'tags',
                 placeholderText   : null,   // Sets `placeholder` attr on input field.
         readOnly          : false,  // Disables editing.
    removeConfirmation: false,  // Require confirmation to remove tags.
    tagLimit          : null,   // Max number of tags allowed (null for unlimited).

                                                      // Used for autocomplete, unless you override `autocomplete.source`.
availableTags     : [],

// Use to override or add any options to the autocomplete widget.
                                                          //
                                                          // By default, autocomplete.source will map to availableTags,
// unless overridden.
    autocomplete: {},

// Shows autocomplete before the user even types anything.
    showAutocompleteOnFocus: false,

// When enabled, quotes are unneccesary for inputting multi-word tags.
allowSpaces: false,

// The below options are for using a single field instead of several
// for our form values.
//
// When enabled, will use a single hidden field for the form,
// rather than one per tag. It will delimit tags in the field
// with singleFieldDelimiter.
//
// The easiest way to use singleField is to just instantiate tag-it
// on an INPUT element, in which case singleField is automatically
// set to true, and singleFieldNode is set to that element. This
// way, you don't need to fiddle with these options.
singleField: false,

// This is just used when preloading data from the field, and for
// populating the field with delimited tags as the user adds them.
singleFieldDelimiter: ',',

// Set this to an input DOM node to use an existing form field.
                                                         // Any text in it will be erased on init. But it will be
                                                                                                               // populated with the text of tags as they are created,
// delimited by singleFieldDelimiter.
//
// If this is not set, we create an input node for it,
// with the name given in settings.fieldName.
singleFieldNode: null,

// Whether to animate tag removals or not.
animate: true,

// Optionally set a tabindex attribute on the input that gets
                                                         // created for tag-it.
tabIndex: null,

// Event callbacks.
    beforeTagAdded      : null,
                          afterTagAdded       : null,

                                                beforeTagRemoved    : null,
                                                                      afterTagRemoved     : null,

                                                                                            onTagClicked        : null,
                                                                                                                  onTagLimitExceeded  : null,


// DEPRECATED:
//
// /!\ These event callbacks are deprecated and WILL BE REMOVED at some
                                                                   // point in the future. They're here for backwards-compatibility.
                                                                                               // Use the above before/after event callbacks instead.
    onTagAdded  : null,
                  onTagRemoved: null,
// `autocomplete.source` is the replacement for tagSource.
tagSource: null
           // Do not use the above deprecated options.
},

_create: function() {
                    // for handling static scoping inside callbacks
var that = this;

// There are 2 kinds of DOM nodes this widget can be instantiated on:
    //     1. UL, OL, or some element containing either of these.
                                                           //     2. INPUT, in which case 'singleField' is overridden to true,
//        a UL is created and the INPUT is hidden.
if (this.element.is('input')) {
    this.tagList = $('<ul></ul>').insertAfter(this.element);
this.options.singleField = true;
this.options.singleFieldNode = this.element;
this.element.addClass('tagit-hidden-field');
} else {
    this.tagList = this.element.find('ul, ol').andSelf().last();
}

this.tagInput = $('<input type="text" />').addClass('ui-widget-content');

if (this.options.readOnly) this.tagInput.attr('disabled', 'disabled');

if (this.options.tabIndex) {
    this.tagInput.attr('tabindex', this.options.tabIndex);
}

if (this.options.placeholderText) {
this.tagInput.attr('placeholder', this.options.placeholderText);
}

if (!this.options.autocomplete.source) {
this.options.autocomplete.source = function(search, showChoices) {
var filter = search.term.toLowerCase();
var choices = $.grep(this.options.availableTags, function(element) {
// Only match autocomplete options that begin with the search term.
// (Case insensitive.)
return (element.toLowerCase().indexOf(filter) === 0);
});
if (!this.options.allowDuplicates) {
choices = this._subtractArray(choices, this.assignedTags());
}
showChoices(choices);
};
}

if (this.options.showAutocompleteOnFocus) {
this.tagInput.focus(function(event, ui) {
that._showAutocomplete();
});

if (typeof this.options.autocomplete.minLength === 'undefined') {
this.options.autocomplete.minLength = 0;
}
}

// Bind autocomplete.source callback functions to this context.
if ($.isFunction(this.options.autocomplete.source)) {
this.options.autocomplete.source = $.proxy(this.options.autocomplete.source, this);
}

// DEPRECATED.
if ($.isFunction(this.options.tagSource)) {
this.options.tagSource = $.proxy(this.options.tagSource, this);
}

this.tagList
.addClass('tagit')
.addClass('ui-widget ui-widget-content ui-corner-all')
// Create the input field.
.append($('<li class="tagit-new"></li>').append(this.tagInput))
.click(function(e) {
var target = $(e.target);
if (target.hasClass('tagit-label')) {
var tag = target.closest('.tagit-choice');
if (!tag.hasClass('removed')) {
that._trigger('onTagClicked', e, {tag: tag, tagLabel: that.tagLabel(tag)});
}
} else {
       // Sets the focus() to the input field, if the user
// clicks anywhere inside the UL. This is needed
// because the input field needs to be of a small size.
that.tagInput.focus();
}
});

// Single field support.
var addedExistingFromSingleFieldNode = false;
if (this.options.singleField) {
if (this.options.singleFieldNode) {
// Add existing tags from the input field.
var node = $(this.options.singleFieldNode);
var tags = node.val().split(this.options.singleFieldDelimiter);
node.val('');
$.each(tags, function(index, tag) {
that.createTag(tag, null, true);
addedExistingFromSingleFieldNode = true;
});
} else {
       // Create our single field input after our list.
    this.options.singleFieldNode = $('<input type="hidden" style="display:none;" value="" name="' + this.options.fieldName + '" />');
this.tagList.after(this.options.singleFieldNode);
}
}

// Add existing tags from the list, if any.
if (!addedExistingFromSingleFieldNode) {
this.tagList.children('li').each(function() {
if (!$(this).hasClass('tagit-new')) {
that.createTag($(this).text(), $(this).attr('class'), true);
$(this).remove();
}
});
}

// Events.
    this.tagInput
    .keydown(function(event) {
                             // Backspace is not detected within a keypress, so it must use keydown.
if (event.which == $.ui.keyCode.BACKSPACE && that.tagInput.val() === '') {
    var tag = that._lastTag();
if (!that.options.removeConfirmation || tag.hasClass('remove')) {
// When backspace is pressed, the last tag is deleted.
that.removeTag(tag);
} else if (that.options.removeConfirmation) {
tag.addClass('remove ui-state-highlight');
}
} else if (that.options.removeConfirmation) {
that._lastTag().removeClass('remove ui-state-highlight');
}

// Comma/Space/Enter are all valid delimiters for new tags,
// except when there is an open quote or if setting allowSpaces = true.
// Tab will also create a tag, unless the tag input is empty,
// in which case it isn't caught.
if (
        (event.which === $.ui.keyCode.COMMA && event.shiftKey === false) ||
event.which === $.ui.keyCode.ENTER ||
(
event.which == $.ui.keyCode.TAB &&
that.tagInput.val() !== ''
) ||
(
event.which == $.ui.keyCode.SPACE &&
that.options.allowSpaces !== true &&
(
$.trim(that.tagInput.val()).replace( /^s*/, '' ).charAt(0) != '"' ||
(
$.trim(that.tagInput.val()).charAt(0) == '"' &&
$.trim(that.tagInput.val()).charAt($.trim(that.tagInput.val()).length - 1) == '"' &&
$.trim(that.tagInput.val()).length - 1 !== 0
)
)
)
) {
// Enter submits the form if there's no text in the input.
if (!(event.which === $.ui.keyCode.ENTER && that.tagInput.val() === '')) {
event.preventDefault();
}

// Autocomplete will create its own tag from a selection and close automatically.
if (!(that.options.autocomplete.autoFocus && that.tagInput.data('autocomplete-open'))) {
that.tagInput.autocomplete('close');
that.createTag(that._cleanedInput());
}
}
}).blur(function(e){
// Create a tag when the element loses focus.
// If autocomplete is enabled and suggestion was clicked, don't add it.
if (!that.tagInput.data('autocomplete-open')) {
that.createTag(that._cleanedInput());
}
});

// Autocomplete.
if (this.options.availableTags || this.options.tagSource || this.options.autocomplete.source) {
    var autocompleteOptions = {
select: function(event, ui) {
    that.createTag(ui.item.value);
// Preventing the tag input to be updated with the chosen value.
return false;
}
};
$.extend(autocompleteOptions, this.options.autocomplete);

// tagSource is deprecated, but takes precedence here since autocomplete.source is set by default,
// while tagSource is left null by default.
autocompleteOptions.source = this.options.tagSource || autocompleteOptions.source;

this.tagInput.autocomplete(autocompleteOptions).bind('autocompleteopen.tagit', function(event, ui) {
    that.tagInput.data('autocomplete-open', true);
}).bind('autocompleteclose.tagit', function(event, ui) {
    that.tagInput.data('autocomplete-open', false);
});

this.tagInput.autocomplete('widget').addClass('tagit-autocomplete');
}
},

destroy: function() {
$.Widget.prototype.destroy.call(this);

this.element.unbind('.tagit');
this.tagList.unbind('.tagit');

this.tagInput.removeData('autocomplete-open');

this.tagList.removeClass([
                             'tagit',
                             'ui-widget',
                             'ui-widget-content',
                             'ui-corner-all',
                             'tagit-hidden-field'
                         ].join(' '));

if (this.element.is('input')) {
this.element.removeClass('tagit-hidden-field');
this.tagList.remove();
} else {
this.element.children('li').each(function() {
if ($(this).hasClass('tagit-new')) {
$(this).remove();
} else {
$(this).removeClass([
                        'tagit-choice',
                        'ui-widget-content',
                        'ui-state-default',
                        'ui-state-highlight',
                        'ui-corner-all',
                        'remove',
                        'tagit-choice-editable',
                        'tagit-choice-read-only'
                    ].join(' '));

$(this).text($(this).children('.tagit-label').text());
}
});

if (this.singleFieldNode) {
this.singleFieldNode.remove();
}
}

return this;
},

_cleanedInput: function() {
// Returns the contents of the tag input, cleaned and ready to be passed to createTag
return $.trim(this.tagInput.val().replace(/^"(.*)"$/, '$1'));
},

_lastTag: function() {
return this.tagList.find('.tagit-choice:last:not(.removed)');
},

_tags: function() {
return this.tagList.find('.tagit-choice:not(.removed)');
},

assignedTags: function() {
// Returns an array of tag string values
var that = this;
var tags = [];
if (this.options.singleField) {
tags = $(this.options.singleFieldNode).val().split(this.options.singleFieldDelimiter);
if (tags[0] === '') {
tags = [];
}
} else {
this._tags().each(function() {
tags.push(that.tagLabel(this));
});
}
return tags;
},

_updateSingleTagsField: function(tags) {
// Takes a list of tag string values, updates this.options.singleFieldNode.val to the tags delimited by this.options.singleFieldDelimiter
$(this.options.singleFieldNode).val(tags.join(this.options.singleFieldDelimiter)).trigger('change');
},

_subtractArray: function(a1, a2) {
var result = [];
for (var i = 0; i < a1.length; i++) {
if ($.inArray(a1[i], a2) == -1) {
result.push(a1[i]);
}
}
return result;
},

tagLabel: function(tag) {
// Returns the tag's string label.
if (this.options.singleField) {
return $(tag).find('.tagit-label:first').text();
} else {
return $(tag).find('input:first').val();
}
},

_showAutocomplete: function() {
    this.tagInput.autocomplete('search', '');
},

_findTagByLabel: function(name) {
    var that = this;
var tag = null;
this._tags().each(function(i) {
if (that._formatStr(name) == that._formatStr(that.tagLabel(this))) {
    tag = $(this);
return false;
}
});
return tag;
},

_isNew: function(name) {
return !this._findTagByLabel(name);
},

_formatStr: function(str) {
if (this.options.caseSensitive) {
return str;
}
return $.trim(str.toLowerCase());
},

_effectExists: function(name) {
return Boolean($.effects && ($.effects[name] || ($.effects.effect && $.effects.effect[name])));
},

createTag: function(value, additionalClass, duringInitialization) {
var that = this;

value = $.trim(value);

if(this.options.preprocessTag) {
value = this.options.preprocessTag(value);
}

if (value === '') {
return false;
}

if (!this.options.allowDuplicates && !this._isNew(value)) {
var existingTag = this._findTagByLabel(value);
if (this._trigger('onTagExists', null, {
    existingTag: existingTag,
    duringInitialization: duringInitialization
}) !== false) {
if (this._effectExists('highlight')) {
existingTag.effect('highlight');
}
}
return false;
}

if (this.options.tagLimit && this._tags().length >= this.options.tagLimit) {
this._trigger('onTagLimitExceeded', null, {duringInitialization: duringInitialization});
return false;
}

var label = $(this.options.onTagClicked ? '<a class="tagit-label"></a>' : '<span class="tagit-label"></span>').text(value);

// Create tag.
    var tag = $('<li></li>') \
    .addClass('tagit-choice ui-widget-content ui-state-default ui-corner-all') \
    .addClass(additionalClass) \
    .append(label);

if (this.options.readOnly){
tag.addClass('tagit-choice-read-only');
} else {
tag.addClass('tagit-choice-editable');
// Button for removing the tag.
var removeTagIcon = $('<span></span>')
.addClass('ui-icon ui-icon-close');
var removeTag = $('<a><span class="text-icon">\xd7</span></a>') // \xd7 is an X
.addClass('tagit-close')
.append(removeTagIcon)
.click(function(e) {
                   // Removes a tag when the little 'x' is clicked. \
    that.removeTag(tag);
});
tag.append(removeTag);
}

// Unless options.singleField is set, each tag has a hidden input field inline.
if (!this.options.singleField) {
var escapedValue = label.html();
tag.append('<input type="hidden" value="' + escapedValue + '" name="' + this.options.fieldName + '" class="tagit-hidden-field" />');
}

if (this._trigger('beforeTagAdded', null, {
    tag: tag,
    tagLabel: this.tagLabel(tag),
    duringInitialization: duringInitialization
}) === false) {
return;
}

if (this.options.singleField) {
var tags = this.assignedTags();
tags.push(value);
this._updateSingleTagsField(tags);
}

// DEPRECATED. \
    this._trigger('onTagAdded', null, tag);

this.tagInput.val('');

// Insert tag. \
    this.tagInput.parent().before(tag);

this._trigger('afterTagAdded', null, {
    tag: tag,
    tagLabel: this.tagLabel(tag),
    duringInitialization: duringInitialization
});

if (this.options.showAutocompleteOnFocus && !duringInitialization) {
setTimeout(function () { that._showAutocomplete(); }, 0);
}
},

removeTag: function(tag, animate) {
    animate = typeof animate === 'undefined' ? this.options.animate : animate;

tag = $(tag);

// DEPRECATED. \
    this._trigger('onTagRemoved', null, tag);

if (this._trigger('beforeTagRemoved', null, {tag: tag, tagLabel: this.tagLabel(tag)}) === false) {
return;
}

if (this.options.singleField) {
var tags = this.assignedTags();
var removedTagLabel = this.tagLabel(tag);
tags = $.grep(tags, function(el){
return el != removedTagLabel;
});
this._updateSingleTagsField(tags);
}

if (animate) {
tag.addClass('removed'); // Excludes this tag from _tags.
var hide_args = this._effectExists('blind') ? ['blind', {direction: 'horizontal'}, 'fast'] : ['fast'];

var thisTag = this;
hide_args.push(function() {
tag.remove();
thisTag._trigger('afterTagRemoved', null, {tag: tag, tagLabel: thisTag.tagLabel(tag)});
});

tag.fadeOut('fast').hide.apply(tag, hide_args).dequeue();
} else {
    tag.remove();
this._trigger('afterTagRemoved', null, {tag: tag, tagLabel: this.tagLabel(tag)});
}

},

removeTagByLabel: function(tagLabel, animate) {
    var toRemove = this._findTagByLabel(tagLabel);
if (!toRemove) {
    throw "No such tag exists with the name '" + tagLabel + "'";
}
this.removeTag(toRemove, animate);
},

removeAll: function() {
                      // Removes all tags.
    var that = this;
this._tags().each(function(index, tag) {
    that.removeTag(tag, false);
});
}

});
})(jQuery);

(function(b){b.widget("ui.tagit",{options:{allowDuplicates:!1,caseSensitive:!0,fieldName:"tags",placeholderText:null,readOnly:!1,removeConfirmation:!1,tagLimit:null,availableTags:[],autocomplete:{},showAutocompleteOnFocus:!1,allowSpaces:!1,singleField:!1,singleFieldDelimiter:",",singleFieldNode:null,animate:!0,tabIndex:null,beforeTagAdded:null,afterTagAdded:null,beforeTagRemoved:null,afterTagRemoved:null,onTagClicked:null,onTagLimitExceeded:null,onTagAdded:null,onTagRemoved:null,tagSource:null},_create:function(){var a= \
this;this.element.is("input")?(this.tagList=b("<ul></ul>").insertAfter(this.element),this.options.singleField=!0,this.options.singleFieldNode=this.element,this.element.addClass("tagit-hidden-field")):this.tagList=this.element.find("ul, ol").andSelf().last();this.tagInput=b('<input type="text" />').addClass("ui-widget-content");this.options.readOnly&&this.tagInput.attr("disabled","disabled");this.options.tabIndex&&this.tagInput.attr("tabindex",this.options.tabIndex);this.options.placeholderText&&this.tagInput.attr("placeholder",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       this.options.placeholderText);this.options.autocomplete.source||(this.options.autocomplete.source=function(a,e){var d=a.term.toLowerCase(),c=b.grep(this.options.availableTags,function(a){return 0===a.toLowerCase().indexOf(d)});this.options.allowDuplicates||(c=this._subtractArray(c,this.assignedTags()));e(c)});this.options.showAutocompleteOnFocus&&(this.tagInput.focus(function(b,d){a._showAutocomplete()}),"undefined"===typeof this.options.autocomplete.minLength&&(this.options.autocomplete.minLength=
0));b.isFunction(this.options.autocomplete.source)&&(this.options.autocomplete.source=b.proxy(this.options.autocomplete.source,this));b.isFunction(this.options.tagSource)&&(this.options.tagSource=b.proxy(this.options.tagSource,this));this.tagList.addClass("tagit").addClass("ui-widget ui-widget-content ui-corner-all").append(b('<li class="tagit-new"></li>').append(this.tagInput)).click(function(d){var c=b(d.target);c.hasClass("tagit-label")?(c=c.closest(".tagit-choice"),c.hasClass("removed")||a._trigger("onTagClicked",
d,{tag:c,tagLabel:a.tagLabel(c)})):a.tagInput.focus()});var c=!1;if(this.options.singleField)if(this.options.singleFieldNode){var d=b(this.options.singleFieldNode),f=d.val().split(this.options.singleFieldDelimiter);d.val("");b.each(f,function(b,d){a.createTag(d,null,!0);c=!0})}else this.options.singleFieldNode=b('<input type="hidden" style="display:none;" value="" name="'+this.options.fieldName+'" />'),this.tagList.after(this.options.singleFieldNode);c||this.tagList.children("li").each(function(){b(this).hasClass("tagit-new")||
(a.createTag(b(this).text(),b(this).attr("class"),!0),b(this).remove())});this.tagInput.keydown(function(c){if(c.which==b.ui.keyCode.BACKSPACE&&""===a.tagInput.val()){var d=a._lastTag();!a.options.removeConfirmation||d.hasClass("remove")?a.removeTag(d):a.options.removeConfirmation&&d.addClass("remove ui-state-highlight")}else a.options.removeConfirmation&&a._lastTag().removeClass("remove ui-state-highlight");if(c.which===b.ui.keyCode.COMMA&&!1===c.shiftKey||c.which===b.ui.keyCode.ENTER||c.which==
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        b.ui.keyCode.TAB&&""!==a.tagInput.val()||c.which==b.ui.keyCode.SPACE&&!0!==a.options.allowSpaces&&('"'!=b.trim(a.tagInput.val()).replace(/^s*/,"").charAt(0)||'"'==b.trim(a.tagInput.val()).charAt(0)&&'"'==b.trim(a.tagInput.val()).charAt(b.trim(a.tagInput.val()).length-1)&&0!==b.trim(a.tagInput.val()).length-1))c.which===b.ui.keyCode.ENTER&&""===a.tagInput.val()||c.preventDefault(),a.options.autocomplete.autoFocus&&a.tagInput.data("autocomplete-open")||(a.tagInput.autocomplete("close"),a.createTag(a._cleanedInput()))}).blur(function(b){a.tagInput.data("autocomplete-open")||
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    a.createTag(a._cleanedInput())});if(this.options.availableTags||this.options.tagSource||this.options.autocomplete.source)d={select:function(b,c){a.createTag(c.item.value);return!1}},b.extend(d,this.options.autocomplete),d.source=this.options.tagSource||d.source,this.tagInput.autocomplete(d).bind("autocompleteopen.tagit",function(b,c){a.tagInput.data("autocomplete-open",!0)}).bind("autocompleteclose.tagit",function(b,c){a.tagInput.data("autocomplete-open",!1)}),this.tagInput.autocomplete("widget").addClass("tagit-autocomplete")},
destroy:function(){b.Widget.prototype.destroy.call(this);this.element.unbind(".tagit");this.tagList.unbind(".tagit");this.tagInput.removeData("autocomplete-open");this.tagList.removeClass("tagit ui-widget ui-widget-content ui-corner-all tagit-hidden-field");this.element.is("input")?(this.element.removeClass("tagit-hidden-field"),this.tagList.remove()):(this.element.children("li").each(function(){b(this).hasClass("tagit-new")?b(this).remove():(b(this).removeClass("tagit-choice ui-widget-content ui-state-default ui-state-highlight ui-corner-all remove tagit-choice-editable tagit-choice-read-only"),
                                                                                                                                                                                                                                                                                                                                                                                                                                                               b(this).text(b(this).children(".tagit-label").text()))}),this.singleFieldNode&&this.singleFieldNode.remove());return this},_cleanedInput:function(){return b.trim(this.tagInput.val().replace(/^"(.*)"$/,"$1"))},_lastTag:function(){return this.tagList.find(".tagit-choice:last:not(.removed)")},_tags:function(){return this.tagList.find(".tagit-choice:not(.removed)")},assignedTags:function(){var a=this,c=[];this.options.singleField?(c=b(this.options.singleFieldNode).val().split(this.options.singleFieldDelimiter),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ""===c[0]&&(c=[])):this._tags().each(function(){c.push(a.tagLabel(this))});return c},_updateSingleTagsField:function(a){b(this.options.singleFieldNode).val(a.join(this.options.singleFieldDelimiter)).trigger("change")},_subtractArray:function(a,c){for(var d=[],f=0;f<a.length;f++)-1==b.inArray(a[f],c)&&d.push(a[f]);return d},tagLabel:function(a){return this.options.singleField?b(a).find(".tagit-label:first").text():b(a).find("input:first").val()},_showAutocomplete:function(){this.tagInput.autocomplete("search",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         "")},_findTagByLabel:function(a){var c=this,d=null;this._tags().each(function(f){if(c._formatStr(a)==c._formatStr(c.tagLabel(this)))return d=b(this),!1});return d},_isNew:function(a){return!this._findTagByLabel(a)},_formatStr:function(a){return this.options.caseSensitive?a:b.trim(a.toLowerCase())},_effectExists:function(a){return Boolean(b.effects&&(b.effects[a]||b.effects.effect&&b.effects.effect[a]))},createTag:function(a,c,d){var f=this;a=b.trim(a);this.options.preprocessTag&&(a=this.options.preprocessTag(a));
if(""===a)return!1;if(!this.options.allowDuplicates&&!this._isNew(a))return a=this._findTagByLabel(a),!1!==this._trigger("onTagExists",null,{existingTag:a,duringInitialization:d})&&this._effectExists("highlight")&&a.effect("highlight"),!1;if(this.options.tagLimit&&this._tags().length>=this.options.tagLimit)return this._trigger("onTagLimitExceeded",null,{duringInitialization:d}),!1;var g=b(this.options.onTagClicked?'<a class="tagit-label"></a>':'<span class="tagit-label"></span>').text(a),e=b("<li></li>").addClass("tagit-choice ui-widget-content ui-state-default ui-corner-all").addClass(c).append(g);
this.options.readOnly?e.addClass("tagit-choice-read-only"):(e.addClass("tagit-choice-editable"),c=b("<span></span>").addClass("ui-icon ui-icon-close"),c=b('<a><span class="text-icon">\u00d7</span></a>').addClass("tagit-close").append(c).click(function(a){f.removeTag(e)}),e.append(c));this.options.singleField||(g=g.html(),e.append('<input type="hidden" value="'+g+'" name="'+this.options.fieldName+'" class="tagit-hidden-field" />'));!1!==this._trigger("beforeTagAdded",null,{tag:e,tagLabel:this.tagLabel(e),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             duringInitialization:d})&&(this.options.singleField&&(g=this.assignedTags(),g.push(a),this._updateSingleTagsField(g)),this._trigger("onTagAdded",null,e),this.tagInput.val(""),this.tagInput.parent().before(e),this._trigger("afterTagAdded",null,{tag:e,tagLabel:this.tagLabel(e),duringInitialization:d}),this.options.showAutocompleteOnFocus&&!d&&setTimeout(function(){f._showAutocomplete()},0))},removeTag:function(a,c){c="undefined"===typeof c?this.options.animate:c;a=b(a);this._trigger("onTagRemoved",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   null,a);if(!1!==this._trigger("beforeTagRemoved",null,{tag:a,tagLabel:this.tagLabel(a)})){if(this.options.singleField){var d=this.assignedTags(),f=this.tagLabel(a),d=b.grep(d,function(a){return a!=f});this._updateSingleTagsField(d)}if(c){a.addClass("removed");var d=this._effectExists("blind")?["blind",{direction:"horizontal"},"fast"]:["fast"],g=this;d.push(function(){a.remove();g._trigger("afterTagRemoved",null,{tag:a,tagLabel:g.tagLabel(a)})});a.fadeOut("fast").hide.apply(a,d).dequeue()}else a.remove(),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     this._trigger("afterTagRemoved",null,{tag:a,tagLabel:this.tagLabel(a)})}},removeTagByLabel:function(a,b){var d=this._findTagByLabel(a);if(!d)throw"No such tag exists with the name '"+a+"'";this.removeTag(d,b)},removeAll:function(){var a=this;this._tags().each(function(b,d){a.removeTag(d,!1)})}})})(jQuery);

</script>


  </head>
    <body>

    <a href="http://github.com/aehlke/tag-it"><img style="position: absolute; top: 0; right: 0; border: 0;" src="http://s3.amazonaws.com/github/ribbons/forkme_right_white_ffffff.png" alt="Fork me on GitHub" /></a>

                                                                                                                                                                                                                   <div id="wrapper">
                                                                                                                                                                                                                           <div id="header">
                                                                                                                                                                                                                                   <h2>Tag-it! Usage Examples</h2>

                                                                                                                                                                                                                                                               <ul id="nav">
                                                                                                                                                                                                                                                                      <li><a href="http://aehlke.github.com/tag-it">&laquo; back to widget home</a></li>
                                                                                                                                                                                                                                                                                                                                                     </ul>
                                                                                                                                                                                                                                                                                                                                                       </div>

                                                                                                                                                                                                                                                                                                                                                         <div id="content">
                                                                                                                                                                                                                                                                                                                                                                 <p>These demo various features of Tag-it. View the source to see how each works.</p>

                                                                                                                                                                                                                                                                                                                                                                                                                                                   <hr>
                                                                                                                                                                                                                                                                                                                                                                                                                                                   <h3>Minimal</h3>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                <form>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                <p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                Vanilla example &mdash; the absolute minimum amount of code required, no configuration. No autocomplete, either. See the other examples for that.
        </p>
<ul id="myTags"></ul>
<input type="submit" value="Submit">
</form>

<hr>
<h3>Single Input Field</h3>
<form>
<p>
Example using a single input form field to hold all the tag values, instead of one per tag (see settings.singleField).
This method is particularly useful if you have a form with one input field for comma-delimited tags that you want to trivially "upgrade" to this fancy jQuery UI widget.
This configuration will also degrade nicely as well for browsers without JS &mdash; the default behavior is to have one input per tag, which does not degrade as well as one comma-delimited input.
</p>
<p>
Normally this input field will be hidden &mdash; we leave it visible here so you can see how it is manipulated by the widget:
    <input name="tags" id="mySingleField" value="Apple, Orange" disabled="true"> <!-- only disabled for demonstration purposes -->
</p>
<ul id="singleFieldTags"></ul>
<input type="submit" value="Submit">
</form>

<hr>
<h3><a name="graceful-degredation"></a>Single Input Field (2)</h3>
<form>
<p>
If you instantiate Tag-it on an INPUT element, it will default to being singleField, with that INPUT element as the singleFieldNode. This is the simplest way to have a gracefully-degrading tag widget.
</p>
<input name="tags" id="singleFieldTags2" value="Apple, Orange">
</form>

<hr>
<h3>Spaces Allowed Without Quotes</h3>
<p>You can already do multiword tags with spaces in them by default, but those must be wrapped in quotes. This option lets you use spaces without requiring the user to quote the input.</p>
<p>There are normally 5 ways to insert a tag after inputting some text: space, comma, enter, selecting an autocomplete option, or defocusing the widget. With the "allowSpaces" option set to true, space no longer inserts a tag, it just adds a space to the current tag input.</p>
                                                                                                                                                                                                                                                                                   <form>
                                                                                                                                                                                                                                                                                   <p></p>
                                                                                                                                                                                                                                                                                        <ul id="allowSpacesTags"></ul>
                                                                                                                                                                                                                                                                                                                   </form>

                                                                                                                                                                                                                                                                                                                     <hr>
                                                                                                                                                                                                                                                                                                                     <h3>Preloading Data in Markup</h3>
                                                                                                                                                                                                                                                                                                                                                    <form>
                                                                                                                                                                                                                                                                                                                                                    <p>
                                                                                                                                                                                                                                                                                                                                                    Using a UL in HTML to prefill the widget with some tags.
</p>
<ul id="myULTags">
<!-- Existing list items will be pre-added to the tags. -->
<li>Tag1</li>
<li>Tag2</li>
</ul>
</form>

<hr>

<h3>Read-only</h3>
<form>
<p>Example of read only tags.</p>
<ul id="readOnlyTags">
<li>Tag1</li>
<li>Tag2</li>
</ul>
</form>

<hr>

<h3>Events</h3>
<form>
<p>Example of tag events. Try adding or removing a tag, adding a duplicate tag, or clicking on a tag's label.</p>
<ul id="eventTags">
<li>Click my label</li>
<li>Remove me</li>
</ul>
</form>
<div id="events_container"></div>

<hr>

<h3>Methods</h3>
<form>
<p>Demos the available widget methods. Click the links below the widget to try them.</p>
<ul id="methodTags"></ul>
<p><a href="#" onclick="var inp=prompt('Enter a tag value to test the createTag method.');$('#methodTags').tagit('createTag', inp);return false;">Create tag</a></p>
<p><a href="#" onclick="var inp=prompt('Enter a tag value to test the removeTagByName method.');$('#methodTags').tagit('removeTagByName', inp);return false;">Remove tag by name</a></p>
<p><a href="#" onclick="$('#methodTags').tagit('removeAll');return false;">Clear tags</a></p>
</form>

<hr>
<h3>Remove Confirmation</h3>
<form>
<p>
When removeConfirmation is enabled the user has to press the backspace key twice to remove the last tag.
</p>
<ul id="removeConfirmationTags">
<li>backspace me</li>
<li>me too</li>
</ul>
</form>

</div>


<div id="footer">
<div class="left">
<p>Built with <a href="http://jquery.com/" target="_blank">jQuery</a> and <a href="http://jqueryui.com/" target="_blank">jQuery UI</a>.</p>
<p>Originally created by <a href="http://levycarneiro.com/">Levy Carneiro Jr</a>. Currently maintained by <a href="http://github.com/aehlke">Alex Ehlke</a>.</p>
</div>
<p class="right weak">Template adopted from <a href="http://orderedlist.com/demos/fancy-zoom-jquery/">orderedlist.com</a></p>
<br class="clear"/>
</div>
</div>
</body>
</html>



{% endblock %}

