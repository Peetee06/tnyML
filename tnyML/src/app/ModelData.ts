export class ModelData
{
    model_id: number;
    description: string;

    constructor(model_id: number, description: string)
    {
        this.model_id = model_id;
        this.description = description;
    }
}