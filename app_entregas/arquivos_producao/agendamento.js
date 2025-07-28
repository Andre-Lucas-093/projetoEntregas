function abrirModal(data) {
  document.getElementById("data-entrega").value = data;
  new bootstrap.Modal(document.getElementById("modalAgendamento")).show();
}
document.getElementById("data-entrega").value = data.toISOString().slice(0, 10);

document.getElementById("form-agendamento").addEventListener("submit", async function (e) {
  e.preventDefault();
  const form = e.target;
  const data = {
    data_entrega: form.data.value,
    vendedor: parseInt(form.vendedor.value),
    veiculo: form.veiculo.value,
    endereco: form.endereco.value
  };

  const res = await fetch("/api/entregas/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  if (res.ok) {
    alert("Entrega agendada!");
    location.reload();  // ou atualize somente o dia
  } else {
    alert("Erro ao agendar.");
  }
});
