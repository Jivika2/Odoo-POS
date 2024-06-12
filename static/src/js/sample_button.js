/**@odoo-module **/

import { PosGlobalState } from 'point_of_sale.models';
import Registries from 'point_of_sale.Registries';


const PosButtonRestrict = (PosGlobalState) => class PosButtonRestrict extends PosGlobalState{
    async _processData(loaddedData){
        await super._processData(...arguments);
        this.visible_backspace_btn = loaddedData['visible_backspace_btn']
    }

}

Registries.Model.extend(PosGlobalState, PosButtonRestrict);