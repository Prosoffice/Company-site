
var waypoint = new Waypoint({
  element: document.getElementById('skills'),
  handler: function() {
      var p = document.querySelectorAll('.progress-bar');
      var otu = (p[0].getAttribute('data-done')+'%')


      if(typeof(p[1]) !== 'undefined'){
      var abuo = (p[1].getAttribute('data-done')+'%')
      }

      if(typeof(p[2]) !== 'undefined'){
      var ato = (p[2].getAttribute('data-done')+'%')
      }

      if(typeof(p[3]) !== 'undefined'){
      var ano = (p[3].getAttribute('data-done')+'%')
      }

      if(typeof(p[4]) !== 'undefined'){
      var ise = (p[4].getAttribute('data-done')+'%')
      }

      if(typeof(p[5]) !== 'undefined'){
      var isii = (p[5].getAttribute('data-done')+'%')
      }

      if(typeof(p[6]) !== 'undefined'){
      var asaa = (p[6].getAttribute('data-done')+'%')
      }
      if(typeof(p[7]) !== 'undefined'){
      var asato = (p[7].getAttribute('data-done')+'%')
      }
      if(typeof(p[8]) !== 'undefined'){
      var itoolu = (p[8].getAttribute('data-done')+'%')
      }
      if(typeof(p[9]) !== 'undefined'){
      var iri = (p[9].getAttribute('data-done')+'%')
      }
      if(typeof(p[10]) !== 'undefined'){
      var iri_otu = (p[10].getAttribute('data-done')+'%')
      }
      if(typeof(p[11]) !== 'undefined'){
      var iri_abuo = (p[11].getAttribute('data-done')+'%')
      }


      p[0].setAttribute(`style`,`width:${otu};transition:1s all`);
      p[1].setAttribute("style",`width:${abuo};transition:1.5s all`);
      p[2].setAttribute("style",`width:${ato};transition:1.7s all`);
      p[3].setAttribute("style",`width:${ano};transition:2s all`);
      p[4].setAttribute("style",`width:${ise};transition:2.3s all`);
      p[5].setAttribute("style",`width:${isii};transition:2.5s all`);
      p[6].setAttribute("style",`width:${asaa};transition:2.7s all`);
      p[7].setAttribute("style",`width:${asato};transition:3.0s all`);
      p[8].setAttribute("style",`width:${itoolu};transition:3.5s all`);
      p[9].setAttribute("style",`width:${iri};transition:4.5s all`);
      p[10].setAttribute("style",`width:${iri_otu};transition:2.5s all`);
      p[11].setAttribute("style",`width:${iri_abuo};transition:1.5s all`);
      },
    offset:'90%'

});




