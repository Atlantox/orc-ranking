const field_translator = {
    'name': 'Nombre',
    'player': 'Jugador',
    'select2-player-container': 'Jugador',
    'deck': 'Mazo',
    'select2-deck-container': 'Mazo',
    'format': 'Formato',
    'select2-format-container': 'Formato',
    'nickname': 'Nickname',
    'username': 'Usuario',
    'password': 'Contraseña',
    'level': 'Tipo',
    'observation': 'Obervación',
    'date': 'Fecha',
}

class FormValidator{
    CleanWrongInputs(){
        // Remove the border-red class from each HTMLElement
        const targets = document.getElementsByClassName('border-red')
           
        Array.from(targets).forEach((target) => {
            target.classList.remove('border-red')
        })        
    }

    // Recieves list of objects of 'key': {'value': value, 'required': true/false}
    // If a value is required and is empty, the input of 'key' id will be red-bordered
    // Returns false if no empty fields were found, otherwise a list of string errors
    FieldsAreEmpty(fields){
        this.CleanWrongInputs()
        var errors = []
        for(let key in fields){
            const targetField = fields[key]
            if ((targetField['value'] === '' || targetField['value'] === undefined) && targetField['required'] === true){
                // El campo es requerido y está vacío
                errors.push('El campo ' + field_translator[key]  + ' no puede estar vacío')
                this.SetRedBorder(key)
            }
        }
        
        if(errors.length === 0)
            return false
        else
            return errors
    }

    // Recieves list of objects of 'key': {'min': value, 'max': value 'value': value}
    // If the min and max are 0, the field will be ignored (to prevent integer.length errors)
    // If no fields are out of the length, returns true, otherwise, a list of string errors
    FieldsMeetsLength(fields){
        var errors = []
        for(let key in fields){
            const targetField = fields[key]
            if(!(targetField['min'] === 0 && targetField['max'] === 0)){
                if ((targetField['value'].length < targetField['min'] || targetField['value'].length > targetField['max']) && targetField['required'] === true){
                    // El campo es requerido y está vacío
                    errors.push('El campo ' + field_translator[key]  + ' no cumple con la longitud de caracteres (' + targetField['min'] + ' - ' + targetField['max'] + ')')
                    this.SetRedBorder(key)
                }                
            }
        }
        
        if(errors.length === 0)
            return true
        else
            return errors
    }

    FieldsAreNumber(fields){

    }

    FieldsAreDate(fields){

    }

    FieldsAreEmail(fields){

    }

    SetRedBorder(elementId){
        const redBorderedTarget = document.getElementById(elementId)
        if(!redBorderedTarget.classList.contains('border-red'))
            redBorderedTarget.classList.add('border-red')
    }
}

export default FormValidator