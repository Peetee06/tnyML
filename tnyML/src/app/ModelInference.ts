export class ModelInference {
    confidence: number;
    prediction: string;

    constructor(
        confidence: number,
        prediction: string) {
        this.confidence = confidence;
        this.prediction = prediction;
    }
}