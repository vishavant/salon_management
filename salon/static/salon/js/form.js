function update_service_amount() {
         var selectedServices = document.querySelectorAll('input[name="services"]:checked');
         var totalAmount = 0;
    
         selectedServices.forEach(function(service) {
             var amount = parseFloat(service.dataset.amount);
             totalAmount += amount;
         });
         document.getElementById('id_service_amount').value = totalAmount.toFixed(2);
     }
