import { useState, useEffect } from "react";
import axios from "axios";
import {
  PieChart, Pie, Tooltip, Cell,
  BarChart, Bar, XAxis, YAxis, CartesianGrid
} from "recharts";

const API = "http://127.0.0.1:8000/api/v1";

const COLORS = ["#4CAF50", "#FF9800", "#F44336", "#2196F3", "#9C27B0"];

function App() {

  const [message, setMessage] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [categories, setCategories] = useState([]);
  const [priorities, setPriorities] = useState([]);
  const [history, setHistory] = useState([]);
  const [reviews, setReviews] = useState([]);
  const [dashboard, setDashboard] = useState(null); 

  // ================= LOAD =================
  const loadData = async () => {
    try {
      setLoading(true);

      const [cat, pri, hist, rev, dash] = await Promise.all([
        axios.get(`${API}/analytics/categories`),
        axios.get(`${API}/analytics/priorities`),
        axios.get(`${API}/history`),
        axios.get(`${API}/review-queue`),
        axios.get(`${API}/analytics`) 
      ]);

      setCategories(
        Object.entries(cat.data).map(([k, v]) => ({
          category: k,
          count: v
        }))
      );

      setPriorities(
        Object.entries(pri.data).map(([k, v]) => ({
          priority: k,
          count: v
        }))
      );

      setHistory(hist.data);
      setReviews(rev.data);
      setDashboard(dash.data); 

    } catch (err) {
      console.error(err);
      setError("⚠️ Backend not reachable");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData();
  }, []);

  // ================= TRIAGE =================
  const handleSubmit = async () => {
    try {
      setLoading(true);
      setError("");

      const res = await axios.post(`${API}/triage`, {
        raw_message: message
      });

      setResult(res.data);
      setMessage("");

      await loadData();

    } catch {
      setError("❌ Triage failed");
    } finally {
      setLoading(false);
    }
  };

  // ================= REVIEW =================
  const approve = async (id) => {
    await axios.post(`${API}/review/approve`, { id });
    loadData();
  };

  const override = async (id) => {
    await axios.post(`${API}/review/override`, {
      id,
      category: "other",
      priority: "P1"
    });
    loadData();
  };

  // ================= UI =================
  return (
    <div style={page}>

      <h1 style={{ textAlign: "center" }}>🚀 TrustAI Dashboard</h1>

      {error && <p style={{ color: "red" }}>{error}</p>}
      {loading && <p>Loading...</p>}

      {/* ================= EVALUATION PANEL ================= */}
      {dashboard && (
        <div style={grid3}>
          <Metric title="Total Messages" value={dashboard.total_messages} color="#2196F3" />
          <Metric title="Review Queue" value={dashboard.review_queue} color="#FF9800" />
          <Metric title="Avg Confidence" value={dashboard.average_confidence} color="#4CAF50" />
        </div>
      )}

      {/* ================= TRIAGE ================= */}
      <div style={card}>
        <h2>Triage Input</h2>

        <textarea
          rows={4}
          style={input}
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />

        <button style={btn} onClick={handleSubmit}>
          Analyze
        </button>

        {result && (
          <pre style={resultBox}>
            {JSON.stringify(result, null, 2)}
          </pre>
        )}
      </div>

      {/* ================= ANALYTICS ================= */}
      <div style={flexRow}>

        <div style={card}>
          <h3>Categories</h3>
          <PieChart width={300} height={300}>
            <Pie data={categories} dataKey="count" nameKey="category" outerRadius={100}>
              {categories.map((_, i) => (
                <Cell key={i} fill={COLORS[i % COLORS.length]} />
              ))}
            </Pie>
            <Tooltip />
          </PieChart>
        </div>

        <div style={card}>
          <h3>Priorities</h3>
          <BarChart width={350} height={300} data={priorities}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="priority" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="count">
              {priorities.map((_, i) => (
                <Cell key={i} fill={COLORS[i % COLORS.length]} />
              ))}
            </Bar>
          </BarChart>
        </div>

      </div>

      {/* ================= HISTORY ================= */}
      <div style={card}>
        <h2>History</h2>
        <table style={table}>
          <thead>
            <tr>
              <th>Message</th>
              <th>Category</th>
              <th>Priority</th>
            </tr>
          </thead>
          <tbody>
            {history.map((item) => (
              <tr key={item.id}>
                <td>{item.message}</td>
                <td>{item.category}</td>
                <td>{item.priority}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* ================= REVIEW ================= */}
      <div style={card}>
        <h2>Review Queue</h2>

        {reviews.length === 0 && <p>No pending reviews</p>}

        {reviews.map((r) => (
          <div key={r.id} style={reviewBox}>
            <b>{r.message}</b>
            <p>{r.ai_category} ({r.ai_priority})</p>

            <button style={approveBtn} onClick={() => approve(r.id)}>
              Approve
            </button>

            <button style={overrideBtn} onClick={() => override(r.id)}>
              Override
            </button>
          </div>
        ))}
      </div>

    </div>
  );
}

// ================= COMPONENT =================
const Metric = ({ title, value, color }) => (
  <div style={{ ...metricCard, borderLeft: `6px solid ${color}` }}>
    <h4>{title}</h4>
    <h2>{value}</h2>
  </div>
);

// ================= STYLES =================
const page = { padding: 30, background: "#f5f7fb", fontFamily: "Segoe UI" };
const flexRow = { display: "flex", gap: 20, marginTop: 20 };
const grid3 = { display: "flex", gap: 20, marginBottom: 20 };

const card = {
  background: "white",
  padding: 20,
  borderRadius: 10,
  boxShadow: "0px 2px 10px rgba(0,0,0,0.1)",
  marginTop: 20
};

const metricCard = {
  flex: 1,
  background: "white",
  padding: 20,
  borderRadius: 10,
  boxShadow: "0px 2px 10px rgba(0,0,0,0.1)"
};

const input = { width: "100%", padding: 10, marginBottom: 10 };
const btn = { padding: "10px 20px", background: "#4CAF50", color: "white", border: "none" };
const resultBox = { background: "#111", color: "#0f0", padding: 10 };

const table = { width: "100%", borderCollapse: "collapse" };

const reviewBox = {
  border: "1px solid #ddd",
  padding: 10,
  borderRadius: 6,
  marginBottom: 10
};

const approveBtn = { background: "#4CAF50", color: "white", marginRight: 10 };
const overrideBtn = { background: "#F44336", color: "white" };

export default App;