import { Example } from "./Example";

import styles from "./Example.module.css";

export type ExampleModel = {
    text: string;
    value: string;
};

const EXAMPLES: ExampleModel[] = [
    {
        text: "Test me on Azure Data Fundamentals",
        value: "Test me on Azure Data Fundamentals"
    },
    { text: "What is a data warehouse?", value: "What is a data warehouse?" },
    { text: "What is an example of batch processing? ", value: "What is an example of batch processing? " },
    { text: "What are the different Azure Cosmos DB APIs?", value: "What are the different Azure Cosmos DB APIs?" },
    { text: "What is the purpose of keys in a relational database?", value: "What is the purpose of keys in a relational database?" },
    { text: "How does a relational database eliminate duplicate data values?", value: "How does a relational database eliminate duplicate data values?" },
    { text: "What are the core concepts of data modeling?", value: "What are the core concepts of data modeling?" }
];

interface Props {
    onExampleClicked: (value: string) => void;
}

export const ExampleList = ({ onExampleClicked }: Props) => {
    return (
        <ul className={styles.examplesNavList}>
            {EXAMPLES.map((x, i) => (
                <li key={i}>
                    <Example text={x.text} value={x.value} onClick={onExampleClicked} />
                </li>
            ))}
        </ul>
    );
};
