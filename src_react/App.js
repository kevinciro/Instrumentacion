import "bootstrap/dist/css/bootstrap.min.css";
import Table from "react-bootstrap/Table";
import Button from "react-bootstrap/Button";
import { axiosInstance } from "./config/config";
import Form from "react-bootstrap/Form";
import { useState } from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Filler,
  Tooltip,
  Legend,
} from "chart.js";
import { Line } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Filler,
  Tooltip,
  Legend
);

function App() {
  const [lugar, setLugar] = useState("");
  const [medicion, setMedicion] = useState("");

  const [object, setObject] = useState([
    {
      _id: 1,
      frecuency: 0.0,
      location: "ninguno",
      hour: null,
      date: null,
    },
  ]);

  // constate para las opciones de la grafica
  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: "top",
      },
      title: {
        display: true,
        text: "Gráfica de Datos",
      },
    },
    scales: {
      y: {
        type: "linear",
        display: true,
        position: "left",
      },
      y1: {
        type: "linear",
        display: true,
        position: "right",
        grid: {
          drawOnChartArea: false,
        },
      },
    },
  };

  // creacion del data
  const [data, setData] = useState({
    labels: ["1"],
    datasets: [
      {
        label: "D",
        data: [1],
        borderColor: "rgb(255, 99, 132)",
        backgroundColor: "rgba(255, 99, 132, 0.5)",
      },
    ],
  });

  function cargarTodosDatos() {
    axiosInstance
      .get("/meditions")
      .then((res) => {
        setObject(res.data);
      })
      .catch((err) => {
        console.error(err);
      });
  }

  function nuevaMedicion(lug) {
    axiosInstance
      .post(`/meditions?lugar=${lug} `)
      .then((res) => {
        setObject(res.data);
      })
      .catch((err) => {
        console.error(err);
      });
  }

  function handleSubmit(event) {
    event.preventDefault();
    console.log(event.target.medicion.value);
    nuevaMedicion(event.target.medicion.value);
  }

  function cargarGrafica() {
    axiosInstance
      .get("/meditions")
      .then((res) => {
        setObject(res.data);
        const datServ = []; // datos de frecuenca
        const labServ = [];

        for (let i = 0; i < res.data.length; i++) {
          labServ.push(res.data[i].date);
          datServ.push(res.data[i].frecuency);
        }

        var plantilla = {
          labels: labServ,
          datasets: [
            {
              fill: true,
              label: "frec",
              data: datServ,
              borderColor: "rgb(255, 99, 132)",
              backgroundColor: "rgba(255, 99, 132, 0.5)",
              yAxisID: "y",
            },
          ],
        };
        setData(plantilla);
      })
      .catch((err) => console.error(err));
  }

  return (
    <div className="App">
      <header className="App-header"></header>

      <h1
        style={{
          width: "100%",
          alignContent: "center",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          padding: "2rem",
        }}
      >
        Medicion frecuencia cardiaca
      </h1>
      <div
        style={{
          width: "100%",
          alignContent: "center",
          display: "flex",
          alignItems: "center",
          justifyContent: "space-around",
        }}
      >
        <Button variant="outline-success" onClick={cargarTodosDatos}>
          Cargar todos
        </Button>
        <Form onSubmit={handleSubmit}>
          <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Control
              name="medicion"
              type="text"
              placeholder="Lugar de medicion"
            />
          </Form.Group>
          <Button variant="success" type="submit">
            Nueva Medicion
          </Button>
        </Form>
        <Button variant="outline-success" onClick={cargarGrafica}>
          ver grafica
        </Button>
      </div>

      <div
        style={{
          width: "100%",
          alignContent: "center",
          display: "flex",
          alignItems: "center",
        }}
      >
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>Frecuencia (latidos/minuto)</th>
              <th>Lugar medicion</th>
              <th>Fecha (dd/mm/yyyy)</th>
              <th>Hora</th>
            </tr>
          </thead>
          <tbody>
            {object.map((o) => {
              return (
                <tr key={o._id}>
                  <td>{o.frecuency.toFixed(2)}</td>
                  <td>{o.location}</td>
                  <td>{o.date}</td>
                  <td>{o.hour}</td>
                </tr>
              );
            })}
          </tbody>
        </Table>
        <Line options={options} data={data} />
      </div>
    </div>
  );
}

export default App;
