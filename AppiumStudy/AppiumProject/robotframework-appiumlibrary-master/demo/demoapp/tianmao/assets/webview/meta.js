(function(){
    var metaElements = document.getElementsByTagName('meta');
    var ret = {};
    if (metaElements.length > 0) {
        for (var iIndex = 0; iIndex < metaElements.length; iIndex++) {
            var element = metaElements[iIndex];
            var attributes = element.attributes, name = element['name'], content = element['content'], id=element['id'], value = attributes['value'];
            if ( name && content && name=='unique-bizid'){
                ret[name] = content;
            }

            if ( id && value && id=='WV.Meta.Nav.HideNavBar'){
                ret[id] = value['value'];
            }
        }
    }
    return JSON.stringify(ret);
})();