class Xiaomi

  def client
    client = InfluxDB::Rails.client
    measurements = client.query('select * from solarwinds WHERE time > now() - 5h').dig(0,"values")
  end

  def aqi
    client.map do |measurement|
      measurement.dig("aqi")
    end
  end

  def time_labels
    full_labels = client.map do |measurement|
      measurement.dig("time")[11..15]
    end
  end


end
